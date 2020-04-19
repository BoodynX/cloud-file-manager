from datetime import datetime
from uuid import UUID

from src.domain.entities.file.file import File
from src.domain.vos.file_content import FileContent
from src.domain.vos.file_type import FileType


class EmptyFileSample:
    FILE_ID = UUID('{12345678-1234-1234-1234-1234567890ab}')
    FILE_NAME = 'empty file name'
    FILE_CONTENT = FileContent()
    FILE_TYPE = FileType('unknown')
    FILE_SIZE = 0
    ADDED = datetime.fromisoformat('2011-11-04T00:05:23')
    SAMPLE_FILE = File(
        id_=FILE_ID,
        name=FILE_NAME,
        content=FILE_CONTENT,
        type_=FILE_TYPE,
        size=FILE_SIZE,
        added=ADDED
    )
