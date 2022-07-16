#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
import run
from emails import generate_email, send_email


def main():
    """Generate an email with the processed report"""
    # Access the product descriptions
    json_product_descriptions, name_weight_list = run.format_product_descriptions()
    print(name_weight_list)
    # Define the report path as /tmp/processed.pdf
    report_file = os.path.join("./processed.pdf")
    # Specify the paragraph format for the product descriptions
    title = (f"Processed Update on {format(datetime.datetime.now().strftime('%Y-%m-%d'))}")
    # Define the format of a paragraph in the report
    for fruit in name_weight_list:
        paragraph = (f"name: {name_weight_list[0]}, weight: {name_weight_list[1]}")

    # Generate the report
    generate_report(report_file, title, paragraph) 


if __name__ == "__main__":
    main()
