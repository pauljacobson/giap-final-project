#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
import run
from emails import generate_email, send_email


def process_data(data):
    """Process the data to be incorporated into the report"""
    report = []
    for item in data:
        report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
    return report


def main():
    """Generate an email with the processed report"""
    # Import the source data to convert into a report
    json_product_descriptions, name_weight_list = run.format_product_descriptions()
    # Generate summary data from a sorted list of items
    summary = process_data(sorted(name_weight_list))
    # Create a paragraph variable for the report
    paragraph = "<br/><br/>".join(summary)
    # Define the report path as /tmp/processed.pdf
    report_file = os.path.join("./processed.pdf")
    # Specify the paragraph format for the product descriptions
    title = (f"Processed Update on {format(datetime.datetime.now().strftime('%Y-%m-%d'))}")
    # Generate the report
    generate_report(report_file, title, paragraph)
    # Generate the email
    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = report_file
    message = generate_email(sender, receiver, subject, body, attachment)
    send_email(message)


if __name__ == "__main__":
    main()
