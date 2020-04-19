from unittest import TestCase

from src.domain.entities.file.location import Location
from tests.sample_data.file_samples.invalid_file_sample import InvalidFileSample as IFS


class TestFileLocation(TestCase):
    def test_invalid_file_path__raise_exception(self):
        self.assertRaises(Exception, Location, IFS.LOCATION)

    def test_root_path__success(self):
        lo = Location('/')
