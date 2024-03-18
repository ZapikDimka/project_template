import unittest
from io import StringIO
from unittest.mock import patch, mock_open
from app.io.input import input_text_from_console, read_file_with_builtin, read_file_with_pandas
from app.io.output import output_text_to_console, write_to_file_with_builtin, write_to_file_with_pandas


class TestIOFunctions(unittest.TestCase):

    def test_input_text_from_console(self):
        with patch('builtins.input', return_value='Test Input'):
            self.assertEqual(input_text_from_console(), 'Test Input')

    def test_read_file_with_builtin_file_found(self):
        test_data = "Test data from file"
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            file_path = "test_file.txt"
            self.assertEqual(read_file_with_builtin(file_path), test_data)
            mock_file.assert_called_once_with(file_path, 'r')

    def test_read_file_with_builtin_file_not_found(self):
        file_path = "nonexistent_file.txt"
        self.assertIsNone(read_file_with_builtin(file_path))

    def test_read_file_with_pandas_file_found(self):
        test_data = "Test data from file"
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            file_path = "test_file.txt"
            self.assertEqual(read_file_with_pandas(file_path), test_data)
            mock_file.assert_called_once_with(file_path, 'r')

    def test_read_file_with_pandas_file_not_found(self):
        file_path = "nonexistent_file.txt"
        self.assertIsNone(read_file_with_pandas(file_path))

    def test_output_text_to_console(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output_text_to_console("Test Output")
            self.assertEqual(mock_stdout.getvalue(), "Test Output\n")

    def test_write_to_file_with_builtin(self):
        test_data = "Test data for file"
        file_path = "test_file.txt"
        with patch('builtins.open', mock_open()) as mock_file:
            write_to_file_with_builtin(file_path, test_data)
            mock_file.assert_called_once_with(file_path, 'w')
            mock_file().write.assert_called_once_with(test_data)

    def test_write_to_file_with_pandas(self):
        test_data = "Test data for file"
        file_path = "test_file.txt"
        with patch('builtins.open', mock_open()) as mock_file:
            write_to_file_with_pandas(file_path, test_data)
            mock_file.assert_called_once_with(file_path, 'w')
            mock_file().write.assert_called_once_with(test_data)


if __name__ == '__main__':
    unittest.main()
