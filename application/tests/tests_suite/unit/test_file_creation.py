from enum import Enum
from unittest import TestCase

from app.domain.entities.file import File
from app.domain.value_objects.file_type import FileType
from app.framework.errors.errors import CustomTypeError


class TestFileCreation(TestCase):
    def test_file_types(self):
        file_type = FileType('')
        self.assertIsInstance(obj=file_type, cls=Enum)

    def test_empty_file(self):
        file = File(content='', type_=FileType(''))
        self.assertIsInstance(obj=file, cls=File)

    def test_incorrect_file_param_types(self):
        self.assertRaises(CustomTypeError, File, content=None, type_=FileType(''))
        self.assertRaises(CustomTypeError, File, content='', type_=None)

