from src.application.utils import tc
from src.domain.entities.file.file import File
from src.domain.vos.location import Location


class FileAggregate:
    def __init__(self, file: File, location: Location):
        tc(location, Location)
        tc(file, File)

        self.location = location
        self.file = file

    @property
    def location(self):
        raise Exception('Direct access to local entity is not allowed')

    @location.setter
    def location(self, location):
        self._location = location
