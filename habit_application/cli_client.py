from habit_application import analytics_processor
from habit_application.habit_processor import HabitProcessor
from utils.colors import BColors
from utils.file_path import FilePath


class Client:
    """
    This is a class that interacts with user and navigates him/her through possible options
    """

    def __init__(self):
        """
        Constructor of the Client class
        """
        self.habit_processor = HabitProcessor()
        self.colors = BColors()
        self.file_path = FilePath()

    def create_new_habit_flow(self):
        """
        Collects data from the user to create a new habit, and sends valid data to the habit_processor.
        """
        habits_names = self.habit_processor.get_names_of_habits_from_list(self.file_path.APP)
        # Prompt the user for the name of the habit
        habit_name = input(f'{self.colors.QUESTION}Please write the name of the habit you would like to achieve: '
                           + self.colors.ENDC)

        # Check if the user entered a habit name
        if habit_name:
            # Check if the habit name already exists in the list
            duplicate = habits_names.count(habit_name)

            if duplicate:
                print(f'{self.colors.WARNING}You already have this habit in your list' + self.colors.ENDC)
            else:
                print(f'{self.colors.QUESTION}Which periodicity would you like to assign for this habit:'
                      + self.colors.ENDC)
                print('1. Daily\n'
                      '2. Weekly')

                # Prompt the user for the habit periodicity
                habit_periodicity = int(input(f'{self.colors.QUESTION}Please put the number: ' + self.colors.ENDC))

                # Check if the user entered a valid periodicity
                if habit_periodicity and habit_periodicity in [1, 2]:
                    self.habit_processor.create_habit(habit_name, habit_periodicity, self.file_path.APP)
                else:
                    print(f'{self.colors.WARNING}You have entered an invalid number' + self.colors.ENDC)
        else:
            print(f'{self.colors.WARNING}You have not entered anything' + self.colors.ENDC)

    def delete_existing_habit_flow(self):
        """
        Displays a list of names of all tracked habits, asks the user for a valid ID,
        and sends it to the habit_processor for deletion.
        """
        print(f'{self.colors.HEADER}Here is the list of all habits:' + self.colors.ENDC)

        habits_names = self.habit_processor.get_names_of_habits_from_list(self.file_path.APP)

        # List all available habits with their corresponding index
        for idx, habit_name in enumerate(habits_names, start=1):
            print(f"{idx}. {habit_name}")

        # Prompt the user for the number of the habit they want to delete
        item_to_delete = int(input(f'{self.colors.QUESTION}'
                                   f'Please write the number of the habit you would like to delete: '
                                   + self.colors.ENDC))

        # Check if the input is a valid integer within the range
        if 1 <= item_to_delete <= len(habits_names):
            habit_name = habits_names[item_to_delete - 1]
            habit_id = self.habit_processor.get_habit_id_by_name(habit_name, self.file_path.APP)

            # Send the habit ID to the habit_processor for deletion
            self.habit_processor.delete_habit(habit_name, habit_id, self.file_path.APP)
        else:
            print(f'{self.colors.WARNING}You have entered an invalid number' + self.colors.ENDC)

    def check_off_habit_flow(self):
        """
        Displays a list of names of all tracked habits, asks the user for a valid ID,
        and sends it to the habit_processor for checking off.
        """
        print(f'{self.colors.HEADER}Here is the list of all habits:' + self.colors.ENDC)
        habits_names = self.habit_processor.get_names_of_habits_from_list(self.file_path.APP)

        # List all available habits with their corresponding index
        for idx, habit_name in enumerate(habits_names, start=1):
            print(f"{idx}. {habit_name}")

        # Prompt the user for the number of the habit they want to check off
        item_to_check_off = int(input(f'{self.colors.QUESTION}'
                                      f'Put the number of the habit you would like to check-off: '
                                      + self.colors.ENDC))

        # Check if the input is a valid integer within the range
        if 1 <= item_to_check_off <= len(habits_names):
            # Send the habit ID to the habit_processor for checking off
            self.habit_processor.add_checked_history(item_to_check_off, self.file_path.APP)
        else:
            print(f'{self.colors.WARNING}You have entered an invalid number' + self.colors.ENDC)

    def run(self):
        """
        Provides a user with a navigation menu for selecting options, calls desired options,
        and closes the application if needed.
        """
        print(f"{self.colors.HEADER}Hello there\n" + self.colors.ENDC)
        while True:
            print("What would you like to do?\n"
                  "1. Create a new habit\n"
                  "2. Delete an existing habit\n"
                  "3. Check-off a habit\n"
                  "4. Get analytics\n"
                  "5. Exit")
            users_input = int(
                input(f'{self.colors.QUESTION}Put a number for the desired operation: ' + self.colors.ENDC))

            if users_input == 1:
                self.create_new_habit_flow()
            elif users_input == 2:
                self.delete_existing_habit_flow()
            elif users_input == 3:
                self.check_off_habit_flow()
            elif users_input == 4:
                analytics_processor.run_analytics()
            elif users_input == 5:
                print(f'{self.colors.HEADER}Goodbye!' + self.colors.ENDC)
                break
            else:
                print(f'{self.colors.WARNING}You have entered an invalid value.')

            print(f'{self.colors.HEADER}Return you to the main menu.\n' + self.colors.ENDC)
