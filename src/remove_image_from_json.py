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

from PIL import Image as pil_Image


def warning_toggle(full_image_string, warning_not_foundry):
    if '/FoundryVTT/Data' in full_image_string.get() or (full_image_string.get() == ''):
        warning_not_foundry.pack_forget()
    else:
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


def save_base64_as_webp(image_directory_save_path: str, name: str, img_bit64: str):
    image_save_path = f"{image_directory_save_path}/{name.replace('json', 'webp')}"
    foundry_split = image_save_path.split("FoundryVTT/Data/")
    world_path = "" if len(foundry_split) < 2 else foundry_split[1]
    # if you haven't specified a location within the foundry directory the img location will be
    # left blank and you'll need to import the image to foundry seperatly

    image_decoded = base64.b64decode(img_bit64)
    webp_img = pil_Image.open(BytesIO(image_decoded)).convert("RGB")

    webp_img.save(image_save_path, "webp")

    return world_path


def pull_components_from_json(json_path: str):
    with open(json_path, "r") as infile:
        scene_data = loads(infile.read())
        # print(scene_data.keys())
        img_base64 = scene_data['img']
        img_base64 = img_base64.replace("data:image/jpeg;base64,", "")
    return scene_data, img_base64


def clean_and_save(json_path: str, image_directory_save_path: str, optimize_image_bool: bool):
    scene_data, img_bit64 = pull_components_from_json(json_path)

    name = path.basename(json_path)

    if optimize_image_bool:
        world_path = save_base64_as_webp(image_directory_save_path=image_directory_save_path, name=name, img_bit64=img_bit64)
        new_format = 'webp'
    else:
        world_path = save_base64_as_jpeg(image_directory_save_path=image_directory_save_path, name=name, img_bit64=img_bit64)
        new_format = 'jpeg'

    scene_data['img'] = world_path

    with open(json_path.replace(".json", "_cleaned.json"), 'w') as outfile:
        outfile.write(dumps(scene_data))

    return f"\"{json_path}\" has been cleaned\nImage saved as {new_format} to {world_path}"
