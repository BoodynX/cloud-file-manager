from datetime import datetime
from uuid import UUID

from app.application.utils import tc
from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_type import FileType


class File:
    def __init__(self, id_: UUID, name: str, extension: str, content: FileContent, type_: FileType, size: int,
                 added: datetime):
        tc(id_, UUID)
        tc(name, str)
        tc(extension, str)
        tc(content, FileContent)
        tc(type_, FileType)
        tc(size, int)
        tc(added, datetime)
        self.id = id_
        self.name = name
        self.extension = extension
        self.content = content
        self.type = type_
        self.size = size
        self.added = added
