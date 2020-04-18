from unittest import TestCase

from src.domain.services.file_manager import FileManager
from tests.sample_data.file_samples import EmptyFileSample
from tests.test_doubles.repositories.files_repository_spy import FilesRepositorySpy


class TestFileManager(TestCase, EmptyFileSample):
    def test_add_empty_file__success(self):
        files_repository_spy = FilesRepositorySpy()
        file_adder = FileManager(repository=files_repository_spy)

        file_adder.add(file=self.EMPTY_FILE)

        self.assertEqual(files_repository_spy.file, self.EMPTY_FILE)
