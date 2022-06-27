#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
import run
from emails import generate_email, send_email


def main():
    """Generate an email with the processed report"""
    # Access the product descriptions
    json_product_descriptions, product_descriptions = run.format_product_descriptions()
    # Define the report path as /tmp/processed.pdf
    report_file = os.path.join("./processed.pdf")
    # Specify the paragraph format for the product descriptions
    title = (f"Processed Update on {format(datetime.datetime.now().strftime('%Y-%m-%d'))}")

    # Loop over the product_descriptions dictionary
    for key, value in product_descriptions.items():
        # Add the product description to the paragraph
        paragraph = f"name: {product_descriptions['name']}\n weight: {product_descriptions['weight']}\n"
        

    generate_report(report_file, title, paragraph) 


if __name__ == "__main__":
    main()
