from unittest import TestCase

from src.domain.vos.folder_name import FolderName, InvalidFolderName


class TestFolderName(TestCase):
    def test_empty_name__raise_invalid_folder_name_exception(self):
        self.assertRaises(InvalidFolderName, FolderName, '')

    def test_whitespace_only_name__raise_invalid_folder_name_exception(self):
        self.assertRaises(InvalidFolderName, FolderName, ' ')

    def test_whitespace_at_the_end__raise_invalid_folder_name_exception(self):
        self.assertRaises(InvalidFolderName, FolderName, 'example ')

    def test_whitespace_at_the_beginning__raise_invalid_folder_name_exception(self):
        self.assertRaises(InvalidFolderName, FolderName, ' example')

    def test_not_allowed_character__raise_invalid_folder_name_exception(self):
        self.assertRaises(InvalidFolderName, FolderName, 'example=')

    def test_all_allowed_characters__raise_invalid_folder_name_exception(self):
        FolderName('1234567890-_ qwertyuiopasdfghjklzxcvbnm')
