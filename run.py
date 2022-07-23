#!/usr/bin/env python3

import requests
import json
from pathlib import Path


def format_product_descriptions():
    """Format product descriptions for the web server as JSON file"""
    product_descriptions = {}
    product_descriptions_list = []
    name_weight_list = []
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
            product_descriptions = {"name": parts[0], "weight": int(parts[1][0:3]), "description": parts[2], "image_name": description.stem + ".jpeg"}
            # Add the product description to the list
            product_descriptions_list.append(product_descriptions)
            
            # Create a list of lists of product names and weights
            name_weight_list.append(f'{parts[0]}, {parts[1]}'.split(', '))

    # Convert the dictionary to JSON
    # json_product_descriptions = json.dumps(product_descriptions_list)
    with open('json_descriptions.json', 'w') as json_fp:
        json.dump(product_descriptions_list, json_fp, indent=2)
        
    # Iterate over items in the product_descriptions_list and 
    # post to http://34.172.81.176/fruits using requests
    for product in product_descriptions_list:
        # Post the product description to the web server
        response = requests.post(
            "http://34.172.81.176/fruits/",
            json=product,
        )
        # Check the response status code
        assert response.status_code == 201
      

    return name_weight_list


if __name__ == "__main__":
    format_product_descriptions()
