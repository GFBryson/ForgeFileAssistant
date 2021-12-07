"""
### Author: BusinessGoose
##  What it does
Script will ask you for a .JSON that is a foundry export file from Dungeon Alchemist
and will take out the image bitstring, then ask you to choose a directory in which to save the image. This script works best if you put it somewhere in your Foundry's `Data` directory ie. `C:Users/YOUR_USERNAME/AppData/Local/Foundry/Data/ ... ` for windows

## Why
This is to help fix an issue with foundry's database where they leave the bitstring raw causing lag issues
and possibly making the world unusable after import.
"""

import base64
from io import BytesIO
from json import loads, dumps
from os import path
from tkinter import *

from PIL import Image as pil_Image

from src.get_paths import get_filepath, get_directorypath
from src.optimize_image import save_base64_as_webp


def warning_toggle(full_image_string, warning_not_foundry):
    is_foundry_img_path = BooleanVar()
    if '/FoundryVTT/Data' in full_image_string.get() or (full_image_string.get() == ''):
        is_foundry_img_path.set(True)
        warning_not_foundry.pack_forget()
    else:
        is_foundry_img_path.set(False)
        warning_not_foundry.pack(side='bottom', fill='x', expand=False)


def save_base64_as_jpeg(image_directory_save_path: str, name: str, img_bit64: str):
    image_save_path = f"{image_directory_save_path}/{name.replace('json', 'jpeg')}"
    foundry_split = image_save_path.split("FoundryVTT/Data/")
    world_path = "" if len(foundry_split) < 2 else foundry_split[1]
    # if you haven't specified a location within the foundry directory the img location will be
    # left blank and you'll need to import the image to foundry separately

    with open(image_save_path, 'wb') as outfile:
        image_decoded = base64.b64decode(img_bit64)
        outfile.write(image_decoded)

    return world_path


def pull_components_from_json(json_path: str):
    with open(json_path, "r") as infile:
        scene_data = loads(infile.read())
        # print(scene_data.keys())
        img_base64 = scene_data['img']
        img_base64 = img_base64.replace("data:image/jpeg;base64,", "")
    return scene_data, img_base64


def clean_and_save(json_path: str, image_directory_save_path: str, optimize_image_bool: bool, warning_image_sz: Text,
                   status_text: StringVar):
    status_text.set("Starting Clean")
    scene_data, img_bit64 = pull_components_from_json(json_path)

    name = path.basename(json_path)
    if optimize_image_bool:
        status_text.set("Optimizing and Saving Image")
        world_path = save_base64_as_webp(image_directory_save_path=image_directory_save_path, name=name,
                                         warning_image_sz=warning_image_sz, img_bit64=img_bit64)
        if world_path == "":
            status_text.set("Saving Image")
            world_path = save_base64_as_jpeg(image_directory_save_path=image_directory_save_path, name=name,
                                             img_bit64=img_bit64)
            new_format = 'jpeg'
        else:
            new_format = 'webp'
    else:
        status_text.set("Saving Image")
        world_path = save_base64_as_jpeg(image_directory_save_path=image_directory_save_path, name=name,
                                         img_bit64=img_bit64)
        new_format = 'jpeg'

    scene_data['img'] = world_path

    status_text.set("Saving Cleaned Scene File")
    with open(json_path.replace(".json", "_cleaned.json"), 'w') as outfile:
        outfile.write(dumps(scene_data))

    status_text.set(f"\"{json_path}\" has been cleaned\nImage saved as {new_format} to {world_path}")


def get_remove_image_from_json_tab(window):
    tab_root = Frame()

    top_frame = Frame(tab_root)
    header = Label(top_frame, text="Foundry Import Cleaner")

    # ------------
    source_frame = Frame(tab_root)
    json_string = StringVar()
    json_label = Label(source_frame, text='Source json file for cleaning').pack(side='left')
    json_path = Entry(source_frame, textvariable=json_string).pack(side='left', expand=True, fill='x')

    browse_button_1 = Button(source_frame, text="Browse",
                             command=lambda: get_filepath(json_string, filetypes=[("json files", "*.json")])).pack(
        side='right')

    source_frame.pack(fill='x', side='top')
    # ------------
    image_destination_frame = Frame(tab_root)
    full_image_string = StringVar()
    full_image_label = Label(image_destination_frame, text='Destination Directory for Image File').pack(side='left')
    full_image_path = Entry(image_destination_frame, textvariable=full_image_string).pack(side='left', expand=True,
                                                                                          fill='x')
    browse_button_2 = Button(image_destination_frame, text="Browse",
                             command=lambda: get_directorypath(full_image_string,
                                                               lambda: warning_toggle(full_image_string,
                                                                                      warning_not_foundry))).pack(
        side='right')
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

    warning_image_sz = Text(bottom_frame, fg='red', bg='yellow', height=10, wrap=WORD)
    warning_image_sz.insert(INSERT,
                            "The image you have selected is too large to convert to .webp format. Your image has been saved as a .jpg")

    warning_not_foundry = Text(bottom_frame, fg='red', bg='yellow', height=5, wrap=WORD)
    warning_not_foundry.insert(INSERT,
                               "WARNING: the selected image destination does not appear to be within Foundry's file system. The clean will still work, however you will need to import the map image to foundry seperatly after importing the scene json")

    status_text = StringVar()
    status_text.set("")
    status_label = Label(bottom_frame, textvariable=status_text)
    trigger_button = Button(bottom_frame, text="clean and save image", command=lambda:
    clean_and_save(json_path=json_string.get(), image_directory_save_path=full_image_string.get(),
                   optimize_image_bool=optimize_image_bool.get(), warning_image_sz=warning_image_sz,
                   status_text=status_text)).pack(side='bottom')
    status_label.pack(side='top')

    bottom_frame.pack(side='bottom')

    tab_root.pack(expand=True, fill='both')

    return tab_root
