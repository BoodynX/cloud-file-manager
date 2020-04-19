from unittest import TestCase

from tests.sample_data.file_samples.empty_file_sample import EmptyFileSample

from src.domain.entities.file.file import File


class TestFileCreation(TestCase):

    def test_given_empty_file___create_file_entity(self):
        file = EmptyFileSample.SAMPLE_FILE
        self.assertIsInstance(obj=file, cls=File)
        self.assertEqual(file.id, EmptyFileSample.FILE_ID)
        self.assertEqual(file.name, EmptyFileSample.FILE_NAME)
        self.assertEqual(file.content, EmptyFileSample.FILE_CONTENT)
        self.assertEqual(file.type, EmptyFileSample.FILE_TYPE)
        self.assertEqual(file.size, EmptyFileSample.FILE_SIZE)
        # self.assertEqual(file.location, EmptyFileSample.LOCATION)  # TODO implement this
        self.assertEqual(file.added, EmptyFileSample.ADDED)
