from abc import ABC, abstractmethod

from app.domain.entities.file import File


class FilesRepositoryInterface(ABC):
    @abstractmethod
    def save(self, file: File) -> None:
        pass