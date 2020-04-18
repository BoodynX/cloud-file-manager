from abc import ABC, abstractmethod

from src.domain.entities.file import File


class FilesRepositoryInterface(ABC):
    @abstractmethod
    def save(self, file: File) -> None:
        pass