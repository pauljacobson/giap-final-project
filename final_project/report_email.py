#!/usr/bin/env python3

import datetime
from pathlib import Path
from reports import generate_report
from run import format_product_descriptions


def generate_email():
    """Generate an email with the processed report"""
    # Access the product descriptions
    product_descriptions = format_product_descriptions()
    # Define the report path as /tmp/processed.pdf
    report_file = Path("/tmp/processed.pdf")
    # Specify the paragraph format for the product descriptions
    paragraph = f"name: {product_descriptions['name']}\n weight: {product_descriptions['weight']}\n"
    title = (
        f"Processed Update on {format(datetime.datetime.now().strftime('%Y-%m-%d'))}"
    )

    # Generate the report
    generate_report(paragraph, title, report_file)


if __name__ == "__main__":
    generate_email()
