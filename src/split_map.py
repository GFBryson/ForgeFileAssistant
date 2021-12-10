from math import floor
from tkinter import *

from PIL import Image as pil_Image

from src.common_frames import get_image_file_picker_frame
from src.optimize_image import save_image_as_webp


def crop_img_to(image: pil_Image, x_1, y_1, x_2, y_2) -> pil_Image:
    cropped_image = image.crop((x_1, y_1, x_2, y_2))
    return cropped_image


def open_and_split_image(image_filepath: str, split_pattern: int):
    image = pil_Image.open(image_filepath).convert("RGB")
    split_images = split_formats[split_pattern](image)
    return split_images


def split_2(image: pil_Image, split_style: int = 0) -> list:
    """
        returns list containing 4 image objects as quadrents from originally submitted image
        """
    dimensions_original = (0, 0) + image.size

    half_width = floor(dimensions_original[2] / 2.0)
    half_height = floor(dimensions_original[3] / 2.0)

    if split_style == 0:
        dimensions_0 = [0, 0, half_width, dimensions_original[3]]  # top left
        dimensions_1 = [half_width + 1, 0, dimensions_original[2], dimensions_original[3]]  # top right

    elif split_style == 1:
        dimensions_0 = [0, 0, dimensions_original[2], half_height]  # top left
        dimensions_1 = [0, half_height + 1, dimensions_original[2], dimensions_original[3]]  # top right

    img0 = crop_img_to(image, *dimensions_0)
    img1 = crop_img_to(image, *dimensions_1)

    return [img0, img1]


def split_3(image: pil_Image)-> list:
    """
            returns list containing 4 image objects as quadrents from originally submitted image
            """
    dimensions_original = (0, 0) + image.size

    third_height = floor(dimensions_original[3] / 3.0)
    two_third_height = floor((dimensions_original[3] / 3.0)*2)

    dimensions_0 = [0, 0, dimensions_original[2], third_height]  # top left
    dimensions_1 = [0, third_height+1, dimensions_original[2], two_third_height]  # top left
    dimensions_2 = [0, two_third_height+1, dimensions_original[2], dimensions_original[3]]  # top left

    img0 = crop_img_to(image, *dimensions_0)
    img1 = crop_img_to(image, *dimensions_1)
    img2 = crop_img_to(image, *dimensions_2)

    return [img0, img1, img2]


def split_4(image: pil_Image) -> list:
    """
    returns list containing 4 image objects as quadrents from originally submitted image
    """
    horz = split_2(image, 0)
    left_2 = split_2(horz[0], 1)
    right_2 = split_2(horz[1], 1)

    return left_2 + right_2


def split_6(image: pil_Image) -> list:
    return []


split_formats = [split_2, split_3, split_4, split_6]


def save_splits(splits: list, generic_path):
    for i in range(len(splits)):
        save_image_as_webp(image=splits[i], image_output_path=generic_path, tag=f"Fragment{i + 1}of{len(splits)}")
        pass


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
