from unittest import TestCase

from tests.sample_data.file_samples.empty_file_sample import EmptyFileSample as EFS

from src.domain.entities.file.file import File


class TestFileCreation(TestCase):

    def test_given_empty_file___create_file_entity(self):
        file = EFS.FILE
        self.assertIsInstance(obj=file, cls=File)
        self.assertEqual(file.id, EFS.FILE_ID)
        self.assertEqual(file.name, EFS.FILE_NAME)
        self.assertEqual(file.content, EFS.FILE_CONTENT)
        self.assertEqual(file.type, EFS.FILE_TYPE)
        self.assertEqual(file.size, EFS.FILE_SIZE)
        # self.assertEqual(file.location, EFS.LOCATION)
        self.assertEqual(file.added, EFS.ADDED)

