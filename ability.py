# __author__ = 'User'


class Ability(object):
    """ The Ability class"""
    def __init__(self, name, level, skill, modifier):
        self._name = name
        self._level = int(level)
        self._effected_skill = skill
        self._modifier = int(modifier)

    def __str__(self):
        return self._name + " " + self._level + " " + self._effected_skill \
            + " " + self._modifier

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_effected_skill(self):
        return self._effected_skill

    def get_modifier(self):
        return self._modifier
