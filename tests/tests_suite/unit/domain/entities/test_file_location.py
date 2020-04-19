from unittest import TestCase

from src.domain.entities.file.location import Location, InvalidFileLocationFormat
from src.domain.vos.folder_name import FolderName


class TestFileLocation(TestCase):

    def test_invalid_file_path__raise_exception(self):
        self.assertRaises(InvalidFileLocationFormat, Location, '')
        self.assertRaises(InvalidFileLocationFormat, Location, 'abc')
        self.assertRaises(InvalidFileLocationFormat, Location, None)
        self.assertRaises(InvalidFileLocationFormat, Location, [''])
        self.assertRaises(InvalidFileLocationFormat, Location, ['abc'])
        self.assertRaises(InvalidFileLocationFormat, Location, [None])

    def test_root_path__success__location_value_empty_list(self):
        location = Location(LocationSamples.ROOT_LOCATION)
        self.assertEqual(location.value, LocationSamples.ROOT_LOCATION)

    def test_single_folder__success__return_list_with_one_FolderName_obj(self):
        location = Location(LocationSamples.SINGLE_FOLDER)
        self.assertEqual(location.value, LocationSamples.SINGLE_FOLDER)

    def test_multiple_sub_folders__success__return_list_with_multiple_FolderName_obj(self):
        location = Location(LocationSamples.MULTIPLE_SUB_FOLDERS)
        self.assertEqual(location.value, LocationSamples.MULTIPLE_SUB_FOLDERS)


class LocationSamples:
    ROOT_LOCATION = []
    SINGLE_FOLDER = [FolderName('folder')]
    MULTIPLE_SUB_FOLDERS = [
        FolderName('folder'),
        FolderName('sub folder'),
        FolderName('sub sub folder')
    ]