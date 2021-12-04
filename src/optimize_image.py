from os.path import splitext
from tkinter import *

from PIL import Image

from src.get_paths import get_filepath

Image.MAX_IMAGE_PIXELS = None

def save_image_as_webp(image_path: str):
    im = Image.open(image_path).convert('RGB')
    save_path, ext = splitext(image_path)
    im.save(save_path + '.webp', 'webp')
    return f"Done. Image saved to {save_path}.webp"


def get_image_optimization_frame(window):
    tab_root = Frame(window)

    source_frame = Frame(tab_root)
    image_filepath_str = StringVar()
    image_filepath_label = Label(source_frame, text='Source Image for Optimization').pack(side='left')
    json_path = Entry(source_frame, textvariable=image_filepath_str).pack(side='left', expand=True, fill='x')

    browse_button_1 = Button(source_frame, text="Browse", command=lambda: get_filepath(image_filepath_str, filetypes=[("Image File", "*.png *.jpeg *.jpg")])).pack(
        side='right')

    source_frame.pack(fill='x', side='top')

    # ------------
    bottom_frame = Frame(tab_root)
    warning_not_foundry = Text(bottom_frame, fg='red', bg='yellow', height=20)
    warning_not_foundry.insert(INSERT,
                               "WARNING: the selected image destination does not appear to be within Foundry's file system. The clean will still work however you will have to import the map image to foundry seperatly after importing the json")

    status_text = StringVar()
    status_text.set("")
    status_label = Label(bottom_frame, textvariable=status_text)
    trigger_button = Button(bottom_frame, text="save image as .webp", command=lambda: status_text.set(
        save_image_as_webp(image_path=image_filepath_str.get()))).pack(side='bottom')
    status_label.pack(side='top')

    bottom_frame.pack(side='bottom')

    tab_root.pack(expand='true', fill='both')
    return tab_root
