from uuid import UUID


class AddFileEvent:
    def __init__(self, file_id: UUID):
        self.file_id = file_id
