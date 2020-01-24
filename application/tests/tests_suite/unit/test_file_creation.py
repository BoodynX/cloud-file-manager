from enum import Enum
from unittest import TestCase

from app.domain.entities.file import File
from app.domain.value_objects.file_type import FileType


class TestFileCreation(TestCase):
    def test_file_types(self):
        file_type = FileType('')
        self.assertIsInstance(obj=file_type, cls=Enum)

    def test_empty_file(self):
        file = File(content='', type_=FileType(''))
        self.assertIsInstance(obj=file, cls=File)

