from tkinter import Frame,StringVar,Label, Entry, Button, BooleanVar, Text, INSERT, Checkbutton

from src.remove_image_from_json import *

def get_remove_image_from_json_tab(window):
    tab_root = Frame()

    top_frame = Frame(tab_root)
    header = Label(top_frame, text="Foundry Import Cleaner")

    # ------------
    source_frame = Frame(tab_root)
    json_string = StringVar()
    json_label = Label(source_frame, text='Source json file for cleaning').pack(side='left')
    json_path = Entry(source_frame, textvariable=json_string).pack(side='left', expand=True, fill='x')

    browse_button_1 = Button(source_frame, text="Browse", command=lambda: get_filepath(json_string, filetypes=[("json files", "*.json")])).pack(side='right')

    source_frame.pack(fill='x', side='top')
    # ------------
    image_destination_frame = Frame(tab_root)
    full_image_string = StringVar()
    full_image_label = Label(image_destination_frame, text='Destination Directory for Image File').pack(side='left')
    full_image_path = Entry(image_destination_frame, textvariable=full_image_string).pack(side='left', expand=True,
                                                                                          fill='x')
    browse_button_2 = Button(image_destination_frame, text="Browse",
                             command=lambda: get_directorypath(full_image_string, lambda: warning_toggle(full_image_string, warning_not_foundry))).pack(side='right')
    image_destination_frame.pack(fill='x', side='top')
    # ------------
    options_frame = Frame(tab_root)
    optimize_image_bool = BooleanVar()
    optimize_image_bool.set(False)
    optimize_image_tick = Checkbutton(options_frame, text="Optimize and save .jpeg image in .webp format",
                                      var=optimize_image_bool).pack()

    options_frame.pack(side='top')
    # ------------
    bottom_frame = Frame(tab_root)
    warning_not_foundry = Text(bottom_frame, fg='red', bg='yellow', height=20)
    warning_not_foundry.insert(INSERT,
                               "WARNING: the selected image destination does not appear to be within Foundry's file system. The clean will still work however you will have to import the map image to foundry seperatly after importing the json")

    status_text = StringVar()
    status_text.set("")
    status_label = Label(bottom_frame, textvariable=status_text)
    trigger_button = Button(bottom_frame, text="clean and save image", command=lambda: status_text.set(
        clean_and_save(json_path=json_string.get(), image_directory_save_path=full_image_string.get(),
                       optimize_image_bool=optimize_image_bool.get()))).pack(side='bottom')
    status_label.pack(side='top')

    bottom_frame.pack(side='bottom')

    tab_root.pack(expand=True, fill='both')

    return tab_root
