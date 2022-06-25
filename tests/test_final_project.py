import pytest

import json

from final_project.changeImage import list_images, reformat_images
from final_project.supplier_image_upload import list_supplier_data, upload_supplier_data
from final_project.run import format_product_descriptions


def test_resize_images():
    """Check whether the images are correctly resized"""
    source_images, current_path = list_images("*.tiff")
    reformat_images(source_images, current_path)
    for image in source_images:
        assert image.resize((600, 400)) == (600, 400)


@pytest.mark.parametrize(
    "check, file_ext", [("image[1]", "*.tiff"), ("image.suffix", "*.jpeg")]
)
def test_change_image(check, file_ext):
    """Test the changeImage function"""
    source_images, current_path = list_images("*.tiff")
    reformat_images(source_images, current_path)
    for image in source_images:
        assert check == file_ext


def test_reformatted_images_dict():
    """Check the reformatted images are in a dictionary"""
    source_images, current_path = list_images("*.jpeg")
    reformat_images(source_images, current_path)
    assert isinstance(reformat_images(source_images, current_path), dict)


def test_images_to_upload_is_list():
    """Check the source images are in a list"""
    assert isinstance(list_supplier_data(), list)


def test_images_to_upload_jpeg():
    """Check the images to upload are jpeg images"""
    for image in list_supplier_data():
        assert image.suffix == ".jpeg"


# def test_descriptions_in_json():
#     """Check the product descriptions are in JSON format"""
#     assert isinstance(format_product_descriptions(), dict)
