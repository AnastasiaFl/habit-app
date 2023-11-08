import unittest
from habit_application.file_processor import FileProcessor
from habit_application.habit_processor import HabitProcessor


class TestCheckedOffHistoryRecordProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = HabitProcessor()
        self.file_processor = FileProcessor()
        self.habit_id = '6'

    def tearDown(self):
        self.delete_checked_off_record()

    def test_create_habit_checked_off_history_record(self):
        # Step 1: Add a checked history record to a habit with the specified ID
        self.processor.add_checked_history(self.habit_id)

        # Step 2: Retrieve the list of habits and find the one with the specified ID
        habits = self.processor.get_list_of_habits()
        self.checked_habit = None
        for habit in habits:
            if habit["id"] == self.habit_id:
                self.checked_habit = habit
                break

        # Step 3: Check the added history record
        checked_history_record = self.checked_habit["checkedHistoryRecords"]
        self.assertEqual(checked_history_record[1]["streak"], "1",
                         "The streak of the added history record should be 1.")

    def delete_checked_off_record(self):
        """
        Deletes a habit history record by ID and updates the habits JSON file.
        """
        habits_json = self.file_processor.read_content()

        for habit in habits_json["habits"]:
            if habit["id"] == self.habit_id:
                records_list = habit["checkedHistoryRecords"]
                if records_list:
                    records_list.pop()

        # Send the updated data to the file_processor to rewrite the file
        self.file_processor.rewrite_content(habits_json)