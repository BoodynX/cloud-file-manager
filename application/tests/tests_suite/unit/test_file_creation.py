from unittest import TestCase

from app.application.errors.general import CustomTypeError
from app.domain.entities.file import File
from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_size import FileSize
from app.domain.value_objects.file_type import FileType


class TestFileCreation(TestCase):
    EMPTY_FILE_CONTENT = FileContent()
    EMPTY_FILE_TYPE = FileType('empty')
    UNKNOWN_FILE_TYPE = FileType('unknown')
    EMPTY_FILE_SIZE = FileSize(0)
    SIZE_IN_BYTES_SAMPLE = 1234567890

    def test_incorrect_file_param_types(self):
        self.assertRaises(CustomTypeError, File, content=None, type_=self.EMPTY_FILE_TYPE, size=self.EMPTY_FILE_SIZE)
        self.assertRaises(CustomTypeError, File, content=self.EMPTY_FILE_CONTENT, type_=None, size=self.EMPTY_FILE_SIZE)
        self.assertRaises(CustomTypeError, File, content=self.EMPTY_FILE_CONTENT, type_=self.EMPTY_FILE_TYPE, size=None)

    def test_file_size(self):
        file_size = FileSize(bytes_=self.SIZE_IN_BYTES_SAMPLE)
        self.assertEqual(file_size.bytes, self.SIZE_IN_BYTES_SAMPLE)

    def test_file(self):
        file = File(
            content=self.EMPTY_FILE_CONTENT,
            type_=self.EMPTY_FILE_TYPE,
            size=self.EMPTY_FILE_SIZE
        )
        self.assertIsInstance(obj=file, cls=File)
        self.assertEqual(file.type, self.EMPTY_FILE_TYPE)
        self.assertNotEqual(file.type, self.UNKNOWN_FILE_TYPE)
