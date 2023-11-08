from habit_processor import HabitProcessor

# global value of habit_processor for further manipulations
habit_processor = HabitProcessor()


def find_longest_streak(habit):
    """
    Find and return the longest streak from a habit's checked history records.

    :param habit: The habit object containing checked history records.
    :return: The longest streak as an integer or 0 if no records are found.
    """
    # Get the list of checked history records from the habit, or an empty list if there are none.
    checked_history = habit.get("checkedHistoryRecords", [])

    # Extract the streak values as integers from the records and store them in a list.
    streaks = [int(record.get("streak", 0)) for record in checked_history]

    # Return the maximum value from the streaks list (the longest streak), or 0 if the list is empty.
    return max(streaks, default=0)


def list_all_habits():
    """
    List and display all the habit names.

    This function retrieves the names of all habits and displays them in a numbered list.

    """
    # Get the list of habit names using the habit_processor.
    habits_names = habit_processor.get_names_of_habits_from_list()

    # Print a header indicating the list of habits.
    print('Here is the list of all habits:')

    # Iterate through the habit names and display them with numbers.
    for idx, habit_name in enumerate(habits_names, start=1):
        print(f"{idx}. {habit_name}")


def list_habits_by_periodicity():
    """
    List habits based on user-chosen periodicity.

    This function prompts the user to choose a periodicity (daily or weekly) and then lists the habits
    based on that periodicity.

    """
    # Prompt the user to choose a periodicity.
    print('Which periodicity would you like to choose:\n'
          '1. Daily\n'
          '2. Weekly')

    # Read the user's input for periodicity.
    users_input_periodicity = int(input('Please put the number: '))

    # Check if the input is valid (1 for daily or 2 for weekly).
    if users_input_periodicity in [1, 2]:
        # Get the list of all habits.
        habits_list = habit_processor.get_list_of_habits()

        # Initialize a counter to number the displayed habits.
        count = 0

        # Iterate through the habits and display those matching the chosen periodicity.
        for habit in habits_list:
            if habit["period"] == str(users_input_periodicity):
                count += 1
                print(f"{count}. {habit['task']}")

        # If no habits match the chosen periodicity, inform the user.
        if count == 0:
            print("You do not have habits of such periodicity")
    else:
        # Inform the user of an invalid input.
        print("You have entered an invalid number")


def list_longest_streaks_for_habits():
    """
    List the longest streaks for each habit.

    This function iterates through the list of habits and calculates the longest streak for each habit,
    then displays it to the user.

    """
    # Get the list of all habits.
    habits_list = habit_processor.get_list_of_habits()

    # Iterate through the habits and calculate the longest streak for each.
    for count, habit in enumerate(habits_list, start=1):
        longest_streak = find_longest_streak(habit)
        print(f"{count}. {habit['task']} has the longest streak of {longest_streak} days")


def get_longest_streak_for_habit():
    """
    Get the longest streak for a specific habit chosen by the user.

    This function presents the user with a list of habits and asks the user to select a habit.
    It then calculates and displays the longest streak for the chosen habit.

    """
    # Get the names of all habits.
    habits_names = habit_processor.get_names_of_habits_from_list()

    # Display the list of all habits.
    print('Here is the list of all habits:')
    for x in range(len(habits_names)):
        print(f"{x + 1}. {habits_names[x]}")

    # Ask the user to select a habit by entering a number.
    item_to_check = int(input('Put the number for which habit you would like to get the longest streak: '))

    # Check if the entered number is valid.
    if 1 <= item_to_check <= len(habits_names):
        # Get the ID of the selected habit.
        habit_id = habit_processor.get_habit_id_by_name(habits_names[item_to_check - 1])

        # Get the list of all habits.
        habits_list = habit_processor.get_list_of_habits()

        # Find the selected habit and calculate its longest streak.
        for habit in habits_list:
            if habit["id"] == habit_id:
                longest_streak = find_longest_streak(habit)
                print(f"{habit['task']} has the longest streak of {longest_streak} days")
    else:
        print('You have passed an invalid value.')


def run_analytics():
    """
    Run analytics operations based on user input.

    This function presents a menu of analytics options to the user and performs the selected operation.
    It allows the user to list habits, filter habits by periodicity, and find the longest streaks.
    """
    print('Here is the list of options to analyze:\n'
          '1. Get the list of all tracked habits\n'
          '2. Get the list of all habits with the same periodicity\n'
          '3. Get the longest streak for all tracked habits\n'
          '4. Get the longest streak for one defined habit')

    # Ask the user to select an analytics option by entering a number.
    users_input = int(input('Put a number for the desired operation: '))

    # Perform the selected analytics operation based on user input.
    if users_input == 1:
        list_all_habits()
    elif users_input == 2:
        list_habits_by_periodicity()
    elif users_input == 3:
        list_longest_streaks_for_habits()
    elif users_input == 4:
        get_longest_streak_for_habit()
    else:
        print('You have entered an invalid option.')
