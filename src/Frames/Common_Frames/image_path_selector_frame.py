from tkinter import *
from src.get_paths import get_filepath

def get_image_file_picker_frame(parent_Frame: Frame):
    source_image_frame = Frame(parent_Frame)
    image_filepath_str = StringVar()
    image_filepath_label = Label(source_image_frame, text='Source Image for Optimization').pack(side='left')
    image_path = Entry(source_image_frame, textvariable=image_filepath_str).pack(side='left', expand=True, fill='x')
    browse_button_1 = Button(source_image_frame, text="Browse", command=lambda: get_filepath(image_filepath_str,
                                                                                             filetypes=[("Image File",
                                                                                                         "*.png *.jpeg *.jpg")])).pack(
        side='right')
    return source_image_frame, image_filepath_str