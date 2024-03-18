import pandas as pd

def output_text_to_console(text):
    """
    Function for outputting text to the console.
    """
    print(text)

def write_to_file_with_builtin(file_path, data):
    """
    Function for writing to a file using Python's built-in capabilities.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print("Data successfully written to file", file_path)
    except IOError:
        print("Error writing to file", file_path)

def write_to_file_with_pandas(file_path, data):
    """
    Function for writing to a file using the pandas library.
    """
    try:
        data.to_csv(file_path, index=False)
        print("Data successfully written to file", file_path)
    except Exception as e:
        print("Error writing to file:", e)