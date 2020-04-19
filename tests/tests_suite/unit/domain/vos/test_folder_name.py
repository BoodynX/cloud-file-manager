from unittest import TestCase

from src.domain.exceptions import ImmutableException
from src.domain.vos.folder_name import FolderName


class TestFolderName(TestCase):
    def test_empty_name__raise_invalid_folder_name_exception(self):
        self.assertRaises(FolderName.InvalidFolderName, FolderName, '')

    def test_whitespace_only_name__raise_invalid_folder_name_exception(self):
        self.assertRaises(FolderName.InvalidFolderName, FolderName, ' ')

    def test_whitespace_at_the_end__raise_invalid_folder_name_exception(self):
        self.assertRaises(FolderName.InvalidFolderName, FolderName, 'example ')

    def test_whitespace_at_the_beginning__raise_invalid_folder_name_exception(self):
        self.assertRaises(FolderName.InvalidFolderName, FolderName, ' example')

    def test_not_allowed_character__raise_invalid_folder_name_exception(self):
        self.assertRaises(FolderName.InvalidFolderName, FolderName, 'example=')

    def test_all_allowed_characters__success_create_instance(self):
        instance = FolderName('1234567890-_ qwertyuiopasdfghjklzxcvbnm')
        self.assertIsInstance(obj=instance, cls=FolderName)

    def test_immutability(self):
        instance = FolderName('1234567890-_ qwertyuiopasdfghjklzxcvbnm')
        self.assertIsInstance(obj=instance, cls=FolderName)
        self.assertRaises(ImmutableException, instance.__setattr__, 'value', 'anything')
