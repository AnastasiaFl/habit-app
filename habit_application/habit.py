from datetime import datetime


class Habit:
    """
    This class represents a new habit.
    """

    def __init__(self, habit_id: int, task: str, periodicity: int):
        """
        Constructor of the Habit class.

        :param habit_id: The ID of the habit to create.
        :param task: The name/task of the habit.
        :param periodicity: The periodicity of the habit to repeat (1 for daily, 2 for weekly).
        """
        self.id = habit_id  # Assign the provided habit ID to the object's ID attribute.
        self.task = task  # Assign the provided task name to the object's task attribute.
        self.periodicity = periodicity  # Assign the provided periodicity to the object's periodicity attribute.

        # Generate the current date and time and store it in ISO 8601 format.
        self.createdAt = datetime.now().isoformat()

        # Initialize an empty list to store the checked history records for the habit.
        self.checkedHistoryRecords = []
