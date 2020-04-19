from typing import List

from src.domain.vos.folder_name import FolderName


class Location:

    def __init__(self, value: List[FolderName]):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: List[FolderName]):
        if not self._validate_file_path(value):
            raise self.InvalidFileLocationFormat()
        self._value = value

    def _validate_file_path(self, value: List[FolderName]):
        if not isinstance(value, list):
            return False

        for folder_name in value:
            if not isinstance(folder_name, FolderName):
                return False

        return True

    class InvalidFileLocationFormat(Exception):
        pass
