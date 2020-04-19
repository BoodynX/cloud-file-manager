from typing import List

from src.domain.utils import tc
from src.domain.vos.folder_name import FolderName


class Location:

    def __init__(self, value: List[FolderName]):
        self.validate_file_path(value)
        self.value = value

    def validate_file_path(self, value):
        tc(obj=value, type_=List)
        for folder_name in value:
            tc(obj=folder_name, type_=FolderName)
