from app.application.interfaces.files_repository_interface import FilesRepositoryInterface
from app.application.utils import tc
from app.domain.entities.file import File


class FileAdder:
    def __init__(self, repository: FilesRepositoryInterface):
        tc(repository, FilesRepositoryInterface)
        self.repository = repository

    def add(self, file: File):
        tc(file, File)
        self.repository.save(file=file)