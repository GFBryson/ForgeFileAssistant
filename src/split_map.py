from math import floor

from PIL import Image as pil_Image

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


def split_3(image: pil_Image) -> list:
    """
            returns list containing 4 image objects as quadrents from originally submitted image
            """
    dimensions_original = (0, 0) + image.size

    third_height = floor(dimensions_original[3] / 3.0)
    two_third_height = floor((dimensions_original[3] / 3.0) * 2)

    dimensions_0 = [0, 0, dimensions_original[2], third_height]  # top left
    dimensions_1 = [0, third_height + 1, dimensions_original[2], two_third_height]  # top left
    dimensions_2 = [0, two_third_height + 1, dimensions_original[2], dimensions_original[3]]  # top left

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
