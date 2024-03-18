def output_text_to_console(text):
    """
    Function for outputting text to the console.

    Parameters:
    text (str): The text to be output to the console.
    """
    print(text)


def write_to_file_with_builtin(file_path, data):
    """
    Function for writing to a file using Python's built-in capabilities.

    Parameters:
    file_path (str): The path to the file to write to.
    data (str): The data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print("Data successfully written to file", file_path)
    except IOError:
        print("Error writing to file", file_path)


def write_to_file_with_pandas(file_path, data):
    """
    Function for writing to a text file using the pandas library.

    Parameters:
    file_path (str): The path to the file to write to.
    data (str): The data to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print("Data successfully written to file", file_path)
    except IOError:
        print("Error writing to file", file_path)
