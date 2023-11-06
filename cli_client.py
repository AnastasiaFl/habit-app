import analytics_processor
from habit_processor import HabitProcessor


class Client:
    """
    This is a class that interacts with user and navigates him/her through possible options
    """

    def __init__(self):
        """
        Constructor of the Client class
        """
        self.habit_processor = HabitProcessor()

    def create_new_habit_flow(self):
        """
        Collects data from the user to create a new habit, and sends valid data to the habit_processor.
        """
        # Prompt the user for the name of the habit
        habit_name = input('Please write the name of the habit you would like to achieve: ')

        # Check if the user entered a habit name
        if habit_name:
            habits_names = self.habit_processor.get_names_of_habits_from_list()
            # Check if the habit name already exists in the list
            duplicate = habits_names.count(habit_name)

            if duplicate:
                print("You already have this habit in your list")
            else:
                print('Which periodicity would you like to assign for this habit:\n'
                      '1. Daily\n'
                      '2. Weekly')

                # Prompt the user for the habit periodicity
                habit_periodicity = int(input('Please put the number: '))

                # Check if the user entered a valid periodicity
                if habit_periodicity and habit_periodicity in [1, 2]:
                    self.habit_processor.create_habit(habit_name, habit_periodicity)
                else:
                    print("You have entered an invalid number")
        else:
            print("You have not entered anything")

    def delete_existing_habit_flow(self):
        """
        Displays a list of names of all tracked habits, asks the user for a valid ID,
        and sends it to the habit_processor for deletion.
        """
        habits_names = self.habit_processor.get_names_of_habits_from_list()
        print('Here is the list of all habits:')

        # List all available habits with their corresponding index
        for idx, habit_name in enumerate(habits_names, start=1):
            print(f"{idx}. {habit_name}")

        # Prompt the user for the number of the habit they want to delete
        item_to_delete = int(input('Please write the number of the habit you would like to delete: '))

        # Check if the input is a valid integer within the range
        if 1 <= item_to_delete <= len(habits_names):
            habit_name = habits_names[item_to_delete - 1]
            habit_id = self.habit_processor.get_habit_id_by_name(habit_name)

            # Send the habit ID to the habit_processor for deletion
            self.habit_processor.delete_habit(habit_name, habit_id)
            print(f'You have successfully deleted the habit: {habit_name}')
        else:
            print("You have entered an invalid number")

    def check_off_habit_flow(self):
        """
        Displays a list of names of all tracked habits, asks the user for a valid ID,
        and sends it to the habit_processor for checking off.
        """
        habits_names = self.habit_processor.get_names_of_habits_from_list()
        print('Here is the list of all habits:')

        # List all available habits with their corresponding index
        for idx, habit_name in enumerate(habits_names, start=1):
            print(f"{idx}. {habit_name}")

        # Prompt the user for the number of the habit they want to check off
        item_to_check_off = int(input('Put the number of the habit you would like to check-off: '))

        # Check if the input is a valid integer within the range
        if 1 <= item_to_check_off <= len(habits_names):
            # Send the habit ID to the habit_processor for checking off
            self.habit_processor.add_checked_history(item_to_check_off)
        else:
            print("You have entered an invalid number")

    def run(self):
        """
        Provides a user with a navigation menu for selecting options, calls desired options,
        and closes the application if needed.
        """
        print('Hello there')
        while True:
            print('What would you like to do?\n'
                  '1. Create a new habit\n'
                  '2. Delete an existing habit\n'
                  '3. Check-off a habit\n'
                  '4. Get analytics\n'
                  '5. Exit')
            users_input = int(input('Put a number for the desired operation: '))

            if users_input == 1:
                self.create_new_habit_flow()
            elif users_input == 2:
                self.delete_existing_habit_flow()
            elif users_input == 3:
                self.check_off_habit_flow()
            elif users_input == 4:
                analytics_processor.run_analytics()
            elif users_input == 5:
                print('Goodbye!')
                break
            else:
                print('You have entered an invalid value.')

            print('Return you to the main menu.')
