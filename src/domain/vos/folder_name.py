import re

from src.domain.exceptions import ImmutableException


class FolderName:
    """
    Folder names can have alphanumeric characters underscores and hyphens.
    Spaces are allowed only between visible characters.
    """
    valid_pattern = re.compile('^([\w-][\w -]*[\w-]+|[\w-])$')

    def __init__(self, name: str):
        self.value = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, name):
        if hasattr(self, '_value'):
            raise ImmutableException()
        if not self.valid_pattern.match(name):
            raise self.InvalidFolderName()
        self._value = name

    class InvalidFolderName(Exception):
        pass



