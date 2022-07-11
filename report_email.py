#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
import run
from emails import generate_email, send_email


def main():
    """Generate an email with the processed report"""
    # Access the product descriptions
    json_product_descriptions, product_descriptions_list = run.format_product_descriptions()
    # print(type(product_descriptions_list))
    # Define the report path as /tmp/processed.pdf
    report_file = os.path.join("./processed.pdf")
    # Specify the paragraph format for the product descriptions
    title = (f"Processed Update on {format(datetime.datetime.now().strftime('%Y-%m-%d'))}")
    # Define the format of a paragraph in the report
    # paragraph = f"name: {json_product_descriptions['name']}\n weight: {json_product_descriptions['weight']}\n"
    paragraph = []
    for fruit in product_descriptions_list:
        # Build a list for the paragraph content
        paragraph.append(f"name: {fruit['name']}\n weight: {fruit['weight']}\n")

    # Generate the report
    generate_report(report_file, title, paragraph) 


if __name__ == "__main__":
    main()
