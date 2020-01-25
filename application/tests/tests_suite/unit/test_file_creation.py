from unittest import TestCase

from app.domain.entities.file import File
from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_type import FileType
from app.framework.errors.errors import CustomTypeError


class TestFileCreation(TestCase):
    EMPTY_FILE_CONTENT = FileContent()
    EMPTY_FILE_TYPE = FileType('empty')
    UNKNOWN_FILE_TYPE = FileType('unknown')

    def test_incorrect_file_param_types(self):
        self.assertRaises(CustomTypeError, File, content=None, type_=self.EMPTY_FILE_TYPE)
        self.assertRaises(CustomTypeError, File, content=self.EMPTY_FILE_CONTENT, type_=None)

    def test_file(self):
        file = File(content=self.EMPTY_FILE_CONTENT, type_=self.EMPTY_FILE_TYPE)
        self.assertIsInstance(obj=file, cls=File)
        self.assertEqual(file.type, self.EMPTY_FILE_TYPE)
        self.assertNotEqual(file.type, self.UNKNOWN_FILE_TYPE)
