#!/usr/bin/env python3

import os
import requests
import json
from pathlib import Path


def format_product_descriptions():
    """Format product descriptions for the web server as JSON file"""
    product_descriptions = {}
    # Specify the product descriptions directory path
    descriptions_path = Path.cwd() / "supplier-data" / "descriptions"
    # Loop over product descriptions in the 
    # product descriptions directory with Path
    for description in descriptions_path.glob("*.txt"):
        with open(description, "r") as desc:
            # Split the product description into parts
            parts = desc.read().split("\n")
            # Create a dictionary of the product description
            product_descriptions["name"] = parts[0]
            product_descriptions["weight"] = parts[1]
            product_descriptions["description"] = parts[2]
            product_descriptions["image"] = description.stem + ".jpeg"

        # Convert the dictionary to JSON
        json_product_descriptions = json.dumps(product_descriptions)

        return json_product_descriptions, product_descriptions


def upload_descriptions():
    """Upload product descriptions to the web server"""
    json_descriptions, product_descriptions = format_product_descriptions()
    url = "http://localhost/fruits"
    # Upload the json_descriptions to the web server
    request = requests.post(url, data=json_descriptions)

    # Check for successful upload
    if request.status_code == 200:
        print("Successfully uploaded product descriptions to the web server")
    else:
        print("Error uploading product descriptions to the web server")


def main():
    """Run the main program"""
    # Format product descriptions for the web server as JSON file
    format_product_descriptions()
    # Upload product descriptions to the web server
    # upload_descriptions()


if __name__ == "__main__":
    main()
