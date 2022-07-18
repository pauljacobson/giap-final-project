#!/usr/bin/env python3

import os
import shutil
import socket
import time

import psutil

from emails import generate_email, send_email


def check_cpu_usage():
    """Check whether CPU usage is below 80%"""
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > 80:
        return True
    return False


def check_available_space():
    """Check whether available space
    is below 20%"""
    disk_usage = shutil.disk_usage("/")
    free_space = disk_usage.free / disk_usage.total * 100
    if free_space < 20:
        return True
    return False


def check_available_memory():
    """Check whether available memory
    is less than 500MB"""
    free_memory = psutil.virtual_memory().available / 2**20
    if free_memory < 500:
        return True
    return False


def check_network_connection():
    """Check whether localhost can
    resolve to 127.0.0.1"""
    if socket.gethostbyname("localhost") == '127.0.0.1':
        return True
    else:
        return False


def main():
    """Run system checks and email report"""
    body = 'Please check your system and resolve the issue as soon as possible.'
    # Set attachment_path to None
    attachment_path = None
    # Check CPU usage
    if check_cpu_usage() is True:
        subject = "Error - CPU usage is over 80%"
        send_email(generate_email("system@localhost", "admin@localhost", subject, body, attachment_path))

    # Check available space
    if check_available_space() is True:
        subject = "Error - Available disk space is less than 20%"
        send_email(generate_email("system@localhost", "admin@localhost", subject, body, attachment_path))

    # Check available memory
    if check_available_memory() is True:
        subject = "Error - Available memory is less than 500MB"
        send_email(generate_email("system@localhost", "admin@localhost", subject, body, attachment_path))

    # Check network connection
    if check_network_connection() is False:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        send_email(generate_email("system@localhost", "admin@localhost", subject, body, attachment_path))


if __name__ == "__main__":
    """Run the main function every 60 seconds"""
    while True:
        main()
        time.sleep(60)
