#!/usr/bin/env python3

import os
import shutil
import socket

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
        return False
    return True


def check_available_memory():
    """Check whether available memory
    is less than 500MB"""
    free_memory = psutil.virtual_memory().available / 2**20
    if free_memory < 500:
        return False
    return True


def check_network_connection():
    """Check whether localhost can
    resolve to 127.0.0.1"""
    if socket.gethostbyname("localhost") == '127.0.0.1':
        return True
    else:
        return False


def main():
    """Run system checks and email report"""
    pass


if __name__ == "__main__":
    main()
