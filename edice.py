from enum import Enum, unique


@unique
class EDice(Enum):
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12