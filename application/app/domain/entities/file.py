from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_size import FileSize
from app.domain.value_objects.file_type import FileType
from app.application.utils import tc


class File:
    def __init__(self, content: FileContent, type_: FileType, size: FileSize):
        tc(content, FileContent)
        tc(type_, FileType)
        tc(size, FileSize)
        self.content = content
        self.type = type_
        self.size = size
