from src.application.interfaces.files_repository_interface import FilesRepositoryInterface
from src.domain.entities.file import File


class FileManager:
    def __init__(self, repository: FilesRepositoryInterface):
        self.repository = repository

    def add(self, file: File):
        self.repository.save(file=file)