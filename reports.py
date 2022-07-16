#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    """Generate a PDF report to email"""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["Normal"])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_body, empty_line])
