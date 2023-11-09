import json
import unittest
from unittest.mock import mock_open, patch
from habit_application.file_processor import FileProcessor
from utils.file_path import FilePath


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.file_processor = FileProcessor()
        self.file_path = FilePath()

    def test_rewrite_content(self):
        # Mock the 'open' built-in function to simulate file writing
        with patch("builtins.open", mock_open()) as mock_file:
            content = {"data": "sample content"}
            self.file_processor.rewrite_content(content, self.file_path.APP)

            # Ensure that 'open' was called with the correct filename and mode
            mock_file.assert_called_once_with('habit_application/data/habits.json', 'w')

            # Ensure that 'json.dump' was called with the correct content and file object
            mock_file.return_value.write.assert_called_once_with(json.dumps(content, indent=4))

    def test_read_content(self):
        # Mock the 'open' built-in function to simulate file reading
        with patch("builtins.open", mock_open(read_data='{"data": "sample content"}')) as mock_file:
            content = self.file_processor.read_content(self.file_path.APP)

            # Ensure that 'open' was called with the correct filename and mode
            open_args, _ = mock_file.call_args
            self.assertEqual(open_args[0], 'habit_application/data/habits.json')
            self.assertEqual(open_args[1], 'r')

            # Ensure that the content is correctly deserialized from JSON
            self.assertEqual(content, {"data": "sample content"})
