from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_type import FileType
from app.framework.utils import tc


class File:
    def __init__(self, content: FileContent, type_: FileType):
        tc(content, FileContent)
        tc(type_, FileType)
        self.content = content
        self.type = type_
