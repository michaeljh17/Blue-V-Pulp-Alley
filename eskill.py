__author__ = 'User'

from enum import Enum, unique


@unique
class ESkill(Enum):
    health = "health"
    brawl = "brawl"
    shoot = "shoot"
    dodge = "dodge"
    might = "might"
    finesse = "finesse"
    cunning = "cunning"
