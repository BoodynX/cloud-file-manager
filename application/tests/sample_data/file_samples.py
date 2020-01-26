from datetime import datetime
from uuid import UUID

from app.domain.entities.file import File
from app.domain.value_objects.file_content import FileContent
from app.domain.value_objects.file_type import FileType


class FileSamples:
    EMPTY_FILE_ID = UUID('{12345678-1234-1234-1234-1234567890ab}')
    EMPTY_FILE_NAME = 'empty file name'
    EMPTY_FILE_EXTENSION = 'empty'
    EMPTY_FILE_CONTENT = FileContent()
    UNKNOWN_FILE_TYPE = FileType('unknown')
    EMPTY_FILE_SIZE = 0
    CURRENT_DATE = datetime.now()
    EMPTY_FILE = File(
        id_=EMPTY_FILE_ID,
        name=EMPTY_FILE_NAME,
        extension=EMPTY_FILE_EXTENSION,
        content=EMPTY_FILE_CONTENT,
        type_=UNKNOWN_FILE_TYPE,
        size=EMPTY_FILE_SIZE,
        added=CURRENT_DATE
    )
