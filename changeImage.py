#!/usr/bin/env python3

from pathlib import Path
from PIL import Image


def list_images(file_extension):
    """List the files in the images directory"""
    source_images = []
    # Specify the images directory path
    current_path = Path.cwd() / "supplier-data" / "images"
    images = current_path.glob(file_extension)
    for image in images:
        source_images.append(image)
    return source_images, current_path


def reformat_images(source_images, current_path):
    """Resize the images to 600x400
    and change image format to jpeg"""
    reformatted_images = {}
    # Specify the images directory path
    # Loop over images in the images directory with Path
    for image in source_images:
        reformatted_image = str(image.stem) + ".jpeg"
        out_path = current_path / reformatted_image
        # Check that the image is not reformatted already
        if image != reformatted_image:
            # Open the image with PIL
            with Image.open(image).convert("RGB") as im:
                # Resize the image to 600x400
                im = im.resize((600, 400))
                # Save the image to the images directory
                im.save(out_path, "JPEG")
            # Add the reformatted image to the reformatted_images dictionary
            reformatted_images[str(image.stem)] = reformatted_image

    return reformatted_images


def main(file_ext):
    """Bringing it all together"""
    source_images, current_path = list_images(file_ext)
    list_images(file_ext)
    reformat_images(source_images, current_path)


if __name__ == "__main__":
    main("*.tiff")
