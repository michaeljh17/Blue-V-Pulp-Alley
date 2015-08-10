__author__ = 'User'


class LeagueModel(object):
    """Top model class"""
    def __init__(self, all_my_abilities="", my_league=""):
        self._all_my_abilities = all_my_abilities
        self._my_league = my_league

    def export_league(self):
        return self._my_league