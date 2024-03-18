import pandas as pd

def input_text_from_console():
    """
    Function for inputting text from the console.
    """
    text = input("Enter text: ")
    return text

def read_file_with_builtin(file_path):
    """
    Function for reading from a file using Python's built-in capabilities.
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
    Function for reading from a file using the pandas library.
    """
    try:
        data = pd.read_csv(file_path)  # Assuming the file is a CSV
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
