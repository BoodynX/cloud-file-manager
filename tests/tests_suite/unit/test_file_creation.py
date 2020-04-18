from unittest import TestCase

from src.domain.entities.file import File
from tests.sample_data.file_samples import EmptyFileSample


class TestFileCreation(TestCase, EmptyFileSample):

    def test_file(self):
        file = self.EMPTY_FILE
        self.assertIsInstance(obj=file, cls=File)
        self.assertEqual(file.id, self.EMPTY_FILE_ID)
        self.assertEqual(file.name, self.EMPTY_FILE_NAME)
        self.assertEqual(file.content, self.EMPTY_FILE_CONTENT)
        self.assertEqual(file.type, self.UNKNOWN_FILE_TYPE)
        self.assertEqual(file.size, self.EMPTY_FILE_SIZE)
        self.assertEqual(file.added, self.CURRENT_DATE)
