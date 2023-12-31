from habit_application.checked_history_record import CheckedHistoryRecord
from habit_application.habit import Habit
from habit_application.file_processor import FileProcessor
from datetime import datetime
from utils.colors import BColors


class HabitProcessor:
    """
    This class works with habit object: creates, reads, deletes, gets properties from it
    """
    def __init__(self):
        """
        Constructor of the HabitProcessor class
        """
        self.file_processor = FileProcessor()
        self.colors = BColors()

    def create_habit(self, task: str, periodicity: int, file_path: str):
        """
        Creates a new habit with provided task and periodicity, updates the habits_json file,
        and sends it to the file_processor.

        :param task: The name of the habit/task the user would like to be done periodically.
        :param periodicity: The periodicity of the habit.
        :param file_path: The path to the file where habit would be created
        """
        # Get the id of the last tracked habit and increment it
        habit_id = int(self.get_last_id(file_path)) + 1

        # Create a new habit object
        habit = Habit(habit_id, task, periodicity)

        # Read the existing habits data
        habits_json = self.file_processor.read_content(file_path)

        # Append the new habit to the list of habits
        habits_json['habits'].append({
            "id": str(habit.id),
            "task": habit.task,
            "createdAt": str(habit.createdAt),
            "period": str(habit.periodicity),
            "checkedHistoryRecords": habit.checkedHistoryRecords
        })

        # Update the habits_json file
        self.file_processor.rewrite_content(habits_json, file_path)

        print(f'{self.colors.OKGREEN}You have successfully added a new habit: ' + self.colors.ENDC)
        print(f'{task} with periodicity: {periodicity}')

    def get_list_of_habits(self, file_path):
        """
        Retrieves the list of habits from content read by the file_processor.

        :param file_path: The path to the file.
        :return: List of habit objects
        """
        habits_json = self.file_processor.read_content(file_path)
        return habits_json["habits"]

    def get_names_of_habits_from_list(self, file_path):
        """
        Retrieves a list of habit names from the list of habit objects.

        :param file_path: The path to the file.
        :return: List of habit names
        """
        habits_list = self.get_list_of_habits(file_path)
        return [habit.get("task") for habit in habits_list]

    def get_last_id(self, file_path):
        """
        Retrieves the ID of the last habit from the list of habit objects.

        :param file_path: The path to the file.
        :return: ID of the last habit
        """
        habits_json_body = self.get_list_of_habits(file_path)
        latest_habit = habits_json_body[-1]
        return latest_habit["id"]

    def get_habit_id_by_name(self, habit_name, file_path):
        """
        Retrieves an ID from the habit objects list by name.

        :param habit_name: The name of the habit/task the user would like to be done periodically.
        :param file_path: The path to the file.
        :return: ID of the habit or None if not found
        """
        habits_list = self.get_list_of_habits(file_path)
        for habit in habits_list:
            if habit["task"] == habit_name:
                return habit["id"]
        return None

    def delete_habit(self, habit_name: str, habit_id: str, file_path):
        """
        Deletes a habit by ID and updates the habits JSON file.

        :param habit_name: The name of the habit/task to delete.
        :param habit_id: The ID of the habit to delete.
        :param file_path: The path to the file.
        """
        habits_json = self.file_processor.read_content(file_path)

        # Create a new habits JSON file without the habit found by ID
        habits_json['habits'] = [record for record in habits_json['habits'] if record["id"] != habit_id]

        # Send the updated data to the file_processor to rewrite the file
        self.file_processor.rewrite_content(habits_json, file_path)

        print(f'{self.colors.OKGREEN}You have successfully deleted the habit: ' + self.colors.ENDC + f'{habit_name}')

    def add_checked_history(self, habit_id, file_path):
        """
        Check off a habit by ID, updating its checked history records.

        :param habit_id: ID of the habit to check off.
        :param file_path: The path to the file.
        """
        habits_json = self.file_processor.read_content(file_path)
        habit = next((h for h in habits_json['habits'] if h["id"] == str(habit_id)))

        habit_name = habit["task"]
        history_records = habit["checkedHistoryRecords"]

        if not history_records:
            history_records = []

        streak = self.get_last_streak(habit)
        checked_off_history_record = CheckedHistoryRecord(streak + 1)
        difference = self.get_days_difference(history_records, checked_off_history_record)

        period = int(habit["period"])
        if period == 1:
            if difference == 0:
                print(self.colors.WARNING + f"You have already checked-off '{habit_name}' habit this day"
                      + self.colors.ENDC)
                return
            elif difference > 1:
                print(self.colors.WARNING + f"You have broken your '{habit_name}' habit" + self.colors.ENDC)
                checked_off_history_record.streak = 1
            elif difference == 1:
                print(self.colors.OKGREEN +
                      f"You have {checked_off_history_record.streak}-day streak for '{habit_name}' habit"
                      + self.colors.ENDC)
            elif difference == -1:
                print(self.colors.OKGREEN + f"It is your 1-day streak for '{habit_name}' habit" + self.colors.ENDC)
        elif period == 2:
            if 0 <= difference < 7:
                print(self.colors.OKGREEN + f"You have already checked-off '{habit_name}' habit this week"
                      + self.colors.ENDC)
                return
            elif difference >= 14:
                print(self.colors.WARNING + f"You have broken your '{habit_name}' habit" + self.colors.ENDC)
                checked_off_history_record.streak = 1
            elif 7 <= difference < 14:
                print(self.colors.OKGREEN +
                      f"You have {checked_off_history_record.streak}-day streak for '{habit_name}' habit"
                      + self.colors.ENDC)
            elif difference == -1:
                print(self.colors.OKGREEN + f"It is your 1-day streak for '{habit_name}' habit" + self.colors.ENDC)

        # Add history record
        history_records.append({
            "occurredAt": str(checked_off_history_record.occurred_at),
            "streak": str(checked_off_history_record.streak)
        })

        habit["checkedHistoryRecords"] = history_records
        self.file_processor.rewrite_content(habits_json, file_path)

    @staticmethod
    def get_last_streak(habit):
        """
        Retrieves the last streak of a habit.

        :param habit: The habit object to retrieve the last streak from.
        :return: The last streak as an integer.
        """
        # Get the list of checked history records for the habit (default to an empty list if not present)
        checked_history = habit.get("checkedHistoryRecords", [])

        # Check if there are any history records
        if checked_history:
            # If there are history records, get the latest record (the last one in the list)
            latest_record = checked_history[-1]

            # Get the streak value from the latest record (default to 0 if not present)
            streak = latest_record.get("streak", 0)

            # Convert the streak to an integer and return it
            return int(streak)
        else:
            # If there are no history records, return 0 to indicate no streak
            return 0

    @staticmethod
    def get_days_difference(habit_history_records, checked_history_record):
        """
        Calculate the difference in days between the last check-off date and the current date.

        :param habit_history_records: List of check-off history records for the habit.
        :param checked_history_record: Object with the current day to check-off the habit.
        :return: The difference in days as an integer. Returns -1 if there are no previous records.
        """
        if not habit_history_records:
            # The history records list is empty, return an appropriate value or handle the case.
            return -1  # You can choose an appropriate value to indicate no previous records

        latest_record_date = habit_history_records[-1]["occurredAt"]
        date1 = latest_record_date[:10]  # Extract the date part, e.g., "2023-11-01"
        date2 = checked_history_record.occurred_at[:10]

        # Parse the date strings to datetime objects (for comparison)
        date_time1 = datetime.strptime(date1, "%Y-%m-%d")
        date_time2 = datetime.strptime(date2, "%Y-%m-%d")

        # Calculate the difference between the two datetime objects
        difference = date_time2 - date_time1

        # Extract the number of days from the difference
        days_difference = difference.days

        return days_difference
