import base64
from io import BytesIO
from os.path import splitext
from tkinter import *

from PIL import Image as pil_Image

from src.get_paths import get_filepath

webp_max_sz_px = 16383  # the max width and height of a .webp file
pil_Image.MAX_IMAGE_PIXELS = webp_max_sz_px ** 2


def check_image_size_from_path(image_path: str, warning: Text = None):
    image = Image.open(image_path)
    return check_image_size(image=image, warning=warning)


def check_image_size(image: pil_Image, warning: Text = None):
    if image.size[1] > webp_max_sz_px or image.size[0] > webp_max_sz_px:
        if warning:
            warning.pack()
        return False
    else:
        if warning:
            warning.pack_forget()
        return False


def save_image_as_webp(image_path: str):
    im = pil_Image.open(image_path).convert('RGB')
    save_path, ext = splitext(image_path)
    im.save(save_path + '.webp', 'webp')
    return f"Done. Image saved to {save_path}.webp"


def save_base64_as_webp(image_directory_save_path: str, name: str, warning_image_sz: Text, img_bit64: str):
    image_save_path = f"{image_directory_save_path}/{name.replace('json', 'webp')}"
    foundry_split = image_save_path.split("FoundryVTT/Data/")
    world_path = "" if len(foundry_split) < 2 else foundry_split[1]
    # if you haven't specified a location within the foundry directory the img location will be
    # left blank and you'll need to import the image to foundry separately

    image_decoded = base64.b64decode(img_bit64)
    img_from_bytes_IO = pil_Image.open(BytesIO(image_decoded)).convert("RGB")

    if check_image_size(img_from_bytes_IO, warning=warning_image_sz):
        img_from_bytes_IO.save(image_save_path, "webp")
    else:  # if the image is too large to be converted to webp save as jpeg
        world_path = ""

    return world_path


def get_image_optimization_frame(window):
    tab_root = Frame(window)

    source_frame = Frame(tab_root)
    image_filepath_str = StringVar()
    image_filepath_label = Label(source_frame, text='Source Image for Optimization').pack(side='left')
    json_path = Entry(source_frame, textvariable=image_filepath_str).pack(side='left', expand=True, fill='x')

    browse_button_1 = Button(source_frame, text="Browse",
                             command=lambda: get_filepath(path_var=image_filepath_str,
                                                          filetypes=[("Image File", "*.png *.jpeg *.jpg")],
                                                          )).pack(
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
