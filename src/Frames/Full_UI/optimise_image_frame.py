from tkinter import Frame, Button, Text, StringVar, INSERT, Label

from src.Frames.Common_Frames.common_frames import get_image_file_picker_frame
from src.optimize_image import save_image_as_webp_from_path


def get_image_optimization_frame(window):
    tab_root = Frame(window)

    source_image_frame, image_filepath_str = get_image_file_picker_frame(tab_root)
    source_image_frame.pack(fill='x', side='top')

    # ------------
    bottom_frame = Frame(tab_root)
    warning_not_foundry = Text(bottom_frame, fg='red', bg='yellow', height=20)
    warning_not_foundry.insert(INSERT,
                               "WARNING: the selected image destination does not appear to be within Foundry's file system. The clean will still work however you will have to import the map image to foundry seperatly after importing the json")

    status_text = StringVar()
    status_text.set("")
    status_label = Label(bottom_frame, textvariable=status_text)
    trigger_button = Button(bottom_frame, text="save image as .webp", command=lambda: status_text.set(
        save_image_as_webp_from_path(image_path=image_filepath_str.get()))).pack(side='bottom')
    status_label.pack(side='top')

    bottom_frame.pack(side='bottom')

    tab_root.pack(expand='true', fill='both')
    return tab_root
