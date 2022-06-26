#!/usr/bin/env python3

import requests
from changeImage import list_images


def list_supplier_data():
    """Upload supplier data to the web server"""
    # Use the list_images function to get the images
    source_images, current_path = list_images("*.jpeg")

    return source_images


def upload_supplier_data(source_images):
    """Upload images in reformatted_images to the web server"""
    url = "http://localhost/upload/"
    for image in source_images:
        with open(image, "rb") as im:
            request = requests.post(url, files={"file": im})

    return request


def main():
    """Collate reformatted images
    and then upload them to the server"""
    list_supplier_data()
    upload_supplier_data(list_supplier_data())


if __name__ == "__main__":
    main()
