from app.application.utils import tc


class FileSize:
    def __init__(self, bytes_: int):
        tc(bytes_, int)
        self.bytes = bytes_
