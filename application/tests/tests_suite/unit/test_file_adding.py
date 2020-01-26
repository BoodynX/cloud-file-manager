from abc import ABC
from unittest import TestCase

from app.application.utils import tc
from app.domain.entities.file import File
from tests.sample_data.file_samples import FileSamples


class FileRepositoryInterface(ABC):
    def save(self, file: File, id_: str) -> None:
        pass


class FileAdder(object):
    def __init__(self, repository: FileRepositoryInterface):
        self.repository = repository

    def handle(self, file: File):
        tc(file, File)
        self.repository.save(file=file, id_='uuid')


# class TestFileAdding(TestCase, FileSamples):
#     def test_file_adding(self):
#         empty_file = File(self.EMPTY_FILE_CONTENT, self.UNKNOWN_FILE_TYPE, self.EMPTY_FILE_SIZE)
#
#         file_adder = FileAdder(repository=)
#         file_adder.handle(file=empty_file)
