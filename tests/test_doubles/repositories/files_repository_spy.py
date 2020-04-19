from src.domain.repositories.files_repository_interface import FilesRepositoryInterface
from src.domain.entities.file.file import File


class FilesRepositorySpy(FilesRepositoryInterface):
    def __init__(self):
        self.file = None

    def save(self, file: File) -> None:
        self.file = file