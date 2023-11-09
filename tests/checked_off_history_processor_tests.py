import unittest
from habit_application.file_processor import FileProcessor
from habit_application.habit_processor import HabitProcessor
from tests.fixtures.file_cleaner import FileCleaner
from utils.file_path import FilePath


class TestCheckedOffHistoryRecordProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = HabitProcessor()
        self.file_processor = FileProcessor()
        self.habit_id = '3'
        self.file_path = FilePath()
        self.file_cleaner = FileCleaner()

    def tearDown(self):
        self.file_cleaner.reload_file_content()

    def test_create_habit_checked_off_history_record(self):
        # Step 1: Add a checked history record to a habit with the specified ID
        self.processor.add_checked_history(self.habit_id, self.file_path.TEST)

        # Step 2: Retrieve the list of habits and find the one with the specified ID
        habits = self.processor.get_list_of_habits(self.file_path.TEST)
        self.checked_habit = None
        for habit in habits:
            if habit["id"] == self.habit_id:
                self.checked_habit = habit
                break

        # Step 3: Check the added history record
        checked_history_record = self.checked_habit["checkedHistoryRecords"]
        self.assertEqual(checked_history_record[1]["streak"], "1",
                         "The streak of the added history record should be 1.")
        