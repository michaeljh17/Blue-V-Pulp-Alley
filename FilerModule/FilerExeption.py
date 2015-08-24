__author__ = 'sef0097'

class FilerException(Exception):
    def __init__(self, value):
        self.value = value
        # Exception.__init__(self, value)

    def __str__(self):
        return repr(self.value)