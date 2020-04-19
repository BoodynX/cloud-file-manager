from datetime import datetime
from uuid import UUID

from src.domain.vos.file_content import FileContent
from src.domain.vos.file_type import FileType


class File:
    def __init__(self, id_: UUID, name: str, content: FileContent, type_: FileType, size: int ,added: datetime):
        self.id = id_
        self.name = name
        self.content = content
        self.type = type_
        self.size = size
        self.added = added
