from tkinter import Frame, IntVar, Radiobutton, W, Button
from src.Frames.Common_Frames.common_frames import get_image_file_picker_frame

def get_split_map_frame(window) -> Frame:
    tab_root = Frame(window)

    # -----
    image_picker_frame, image_filepath_str = get_image_file_picker_frame(tab_root)
    image_picker_frame.pack(fill='x', side='top')
    # -----
    radio_selection_frame = Frame(tab_root)
    radio_selection_var = IntVar()
    radio_selection_var.set(2)
    R1 = Radiobutton(radio_selection_frame, text="2", variable=radio_selection_var, value=0, command=None)
    R1.pack(anchor=W)
    R2 = Radiobutton(radio_selection_frame, text="3", variable=radio_selection_var, value=1, command=None)
    R2.pack(anchor=W)
    R3 = Radiobutton(radio_selection_frame, text="4", variable=radio_selection_var, value=2, command=None)
    R3.pack(anchor=W)
    R4 = Radiobutton(radio_selection_frame, text="6", variable=radio_selection_var, value=3, command=None)
    R4.pack(anchor=W)

    radio_selection_frame.pack()

    # -----
    process_image_frame = Frame(tab_root)
    process_image_button = Button(process_image_frame, text="Split and Save Image",
                                  command=lambda: save_splits(
                                      open_and_split_image(image_filepath=image_filepath_str.get(),
                                                           split_pattern=radio_selection_var.get()),
                                      image_filepath_str.get()))
    process_image_button.pack()
    process_image_frame.pack()

    tab_root.pack(expand=True, fill='both')
    return tab_root