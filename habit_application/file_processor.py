import json


class FileProcessor:
    """
    This class deals with file
    """

    @staticmethod
    def rewrite_content(content, file_path):
        """
        Writes the provided content to the 'habits.json' file.

        :param file_path: Path to the file
        :param content: The content to write to the file.
        """
        with open(file_path, 'w') as file:
            # Serialize the content to JSON format and write it to the file with proper indentation.
            json.dump(content, file, indent=4)
            file.close()

        return

    @staticmethod
    def read_content(file_path):
        """
        Reads and returns the content from the 'habits.json' file.

        :param file_path: Path to the file
        :return: The content read from the file.
        """
        with open(file_path, 'r') as file:
            # Deserialize the JSON content from the file and return it.
            habits_json = json.load(file)
            file.close()

        return habits_json
