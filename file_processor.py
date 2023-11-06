import json


class FileProcessor:
    """
    This class deals with file
    """

    @staticmethod
    def rewrite_content(content):
        """
        Writes the provided content to the 'habits.json' file.

        :param content: The content to write to the file.
        """
        with open('habits.json', 'w') as file:
            # Serialize the content to JSON format and write it to the file with proper indentation.
            json.dump(content, file, indent=4)

    @staticmethod
    def read_content():
        """
        Reads and returns the content from the 'habits.json' file.

        :return: The content read from the file.
        """
        with open('habits.json', 'r') as file:
            # Deserialize the JSON content from the file and return it.
            habits_json = json.load(file)
            return habits_json
