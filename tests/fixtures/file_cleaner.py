from habit_application.file_processor import FileProcessor
from utils.file_path import FilePath


class FileCleaner:
    file_processor = FileProcessor()
    file_path = FilePath()

    def reload_file_content(self):
        content = self.file_processor.read_content(self.file_path.TEST_RELOAD)
        self.file_processor.rewrite_content(content, self.file_path.TEST)
