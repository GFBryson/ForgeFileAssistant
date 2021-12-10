from os.path import splitext
from tkinter import *

from PIL import Image as pil_Image

from src.common_frames import get_image_file_picker_frame

Image.MAX_IMAGE_PIXELS = None

def save_image_as_webp_from_path(image_path: str):
    im = Image.open(image_path).convert('RGB')
    return save_image_as_webp(im, image_path)


def save_image_as_webp(image: pil_Image, image_output_path: str, tag: str = ""):
    save_path, ext = splitext(image_output_path)
    image.save(f'{save_path}_{tag}.webp', 'webp')
    return f"Done. Image saved to {save_path}.webp"



