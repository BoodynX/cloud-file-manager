import re


class Location:
    root_path = '/'
    location_pattern = re.compile('^/(?!\s*$)[0-9a-zA-Z/ -]+[0-9a-zA-Z]$')

    def __init__(self, value=str):
        self.validate_file_path(value)
        self.value = value

    def validate_file_path(self, value):
        if value == self.root_path:
            return True
        if not self.location_pattern.match(value):
            raise Exception()
