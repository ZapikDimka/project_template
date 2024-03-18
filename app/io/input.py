import os

import pandas as pd


def input_text_from_console():
    """
    Function for inputting text from the console.

    Returns:
    str: The text entered by the user.
    """
    text = input("Enter text: ")
    return text


def read_file_with_builtin(file_path):
    """
    Function for reading from a file using Python's built-in capabilities.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None


def read_file_with_pandas(file_path):
    """
    Function for reading from a text file using the pandas library.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

