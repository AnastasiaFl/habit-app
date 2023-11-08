import unittest
from habit_application.habit_processor import HabitProcessor


class TestHabitProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = HabitProcessor()
        self.habit_name = "Test Habit"
        self.habit_periodicity = 1
        self.last_habit_id = int(self.processor.get_last_id())
        self.processor.create_habit(self.habit_name, self.habit_periodicity)
        self.habits = self.processor.get_list_of_habits()
        self.checked_habit = self.habits[-1]

    def tearDown(self):
        habit_id = self.processor.get_last_id()
        self.processor.delete_habit("Test Habit", habit_id)

    def test_create_habit_id_incremented(self):
        self.assertEqual(int(self.checked_habit['id']), self.last_habit_id + 1)

    def test_create_habit_task_and_periodicity(self):
        self.assertEqual(self.checked_habit["task"], self.habit_name)
        self.assertEqual(int(self.checked_habit["period"]), self.habit_periodicity)

