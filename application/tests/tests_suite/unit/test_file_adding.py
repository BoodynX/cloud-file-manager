from unittest import TestCase

from app.application.interactors.file_adder import FileAdder
from tests.sample_data.file_samples import FileSamples
from tests.test_doubles.repositories.files_repository_spy import FilesRepositorySpy


class TestFileAdding(TestCase, FileSamples):
    def test_file_adding(self):
        files_repository_spy = FilesRepositorySpy()
        file_adder = FileAdder(repository=files_repository_spy)

        file_adder.add(file=self.EMPTY_FILE)

        self.assertEqual(files_repository_spy.file, self.EMPTY_FILE)
