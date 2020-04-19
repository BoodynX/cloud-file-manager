from typing import List

from src.domain.utils import tc, CustomTypeError
from src.domain.vos.folder_name import FolderName


class Location:

    def __init__(self, value: List[FolderName]):
        if not self._validate_file_path(value):
            raise InvalidFileLocationFormat()
        self.value = value

    def _validate_file_path(self, value: List[FolderName]):
        try:
            tc(obj=value, type_=list)
            for folder_name in value:
                tc(obj=folder_name, type_=FolderName)
        except CustomTypeError:

            return False

        return True


class InvalidFileLocationFormat(Exception):
    pass
