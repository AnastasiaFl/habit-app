import unittest
from habit_application.habit_processor import HabitProcessor
from tests.fixtures.file_cleaner import FileCleaner
from utils.file_path import FilePath


class TestHabitProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = HabitProcessor()
        self.file_path = FilePath()
        self.file_cleaner = FileCleaner()
        self.habit_name = "Test Habit"
        self.habit_periodicity = 1
        self.last_habit_id = int(self.processor.get_last_id(self.file_path.TEST))
        self.processor.create_habit(self.habit_name, self.habit_periodicity, self.file_path.TEST)
        self.habits = self.processor.get_list_of_habits(self.file_path.TEST)
        self.checked_habit = self.habits[-1]

    def tearDown(self):
        self.file_cleaner.reload_file_content()

    def test_create_habit_id_incremented(self):
        self.assertEqual(int(self.checked_habit['id']), self.last_habit_id + 1)

    def test_create_habit_task_and_periodicity(self):
        self.assertEqual(self.checked_habit["task"], self.habit_name)
        self.assertEqual(int(self.checked_habit["period"]), self.habit_periodicity)
