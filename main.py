import os
import pandas as pd
from app.io.input import input_text_from_console, read_file_with_builtin, read_file_with_pandas
from app.io.output import output_text_to_console, write_to_file_with_builtin, write_to_file_with_pandas

def main():
    # Використовуємо функції з input.py
    text_from_console = input_text_from_console()
    text_from_builtin_file = read_file_with_builtin('file.txt')
    text_from_pandas_file = read_file_with_pandas('file.txt')

    # Використовуємо функції з output.py
    output_text_to_console(text_from_console)
    write_to_file_with_builtin('output_builtin.txt', text_from_builtin_file)
    write_to_file_with_pandas('output_pandas.txt', text_from_pandas_file)

if __name__ == "__main__":
    main()
