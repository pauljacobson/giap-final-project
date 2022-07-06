#!/usr/bin/env python3

import requests
import json
from pathlib import Path


def format_product_descriptions():
    """Format product descriptions for the web server as JSON file"""
    product_descriptions = {}
    product_descriptions_list = []
    # Specify the product descriptions directory path
    descriptions_path = Path.cwd() / "supplier-data" / "descriptions"
    # Loop over product descriptions in the 
    # product descriptions directory with Path
    descriptions = descriptions_path.glob("*.txt")

    for description in descriptions:
        # Read the product description
        with open(description, "r") as desc:
            # Split the product description into parts
            parts = desc.read().split("\n")
            # Compile the product_descriptions dictionary 
            product_descriptions = {"name": parts[0], "weight": parts[1], "description": parts[2], "image": description.stem + ".jpeg"}
            # Add the product description to the list
            product_descriptions_list.append(product_descriptions)

    # Convert the dictionary to JSON
    json_product_descriptions = json.dumps(product_descriptions_list)
    with open('json_descriptions.json', 'w') as json_fp:
        json.dump(product_descriptions_list, json_fp, indent=2)

    # return json_product_descriptions, product_descriptions
    return json_product_descriptions, product_descriptions

def upload_descriptions():
    """Upload product descriptions to the web server"""
    json_descriptions, product_descriptions = format_product_descriptions()
    # Specify the product descriptions JSON file
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
    upload_descriptions()


if __name__ == "__main__":
    main()
