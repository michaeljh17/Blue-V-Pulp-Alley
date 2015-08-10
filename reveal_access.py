__author__ = 'User'

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initial=None, name='var'):
        self.val = initial
        self.name = name

    def __get__(self, obj, objtype):
        print ('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print ('Updating', self.name)
        self.val = val
