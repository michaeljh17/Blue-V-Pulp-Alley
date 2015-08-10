__author__ = 'User'


class InputException(Exception):
    def __init__(self, value):
        self.value = value
        # Exception.__init__(self, value)

    def __str__(self):
        return repr(self.value)

    # print("The user has entered the incorrect input")
