from app.application.interfaces.files_repository_interface import FilesRepositoryInterface
from app.domain.entities.file import File


class FilesRepositorySpy(FilesRepositoryInterface):
    def __init__(self):
        self.file = None

    def save(self, file: File) -> None:
        self.file = file