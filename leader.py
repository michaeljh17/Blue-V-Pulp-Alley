from character import Character
from character_exception import CharacterException
from edice import EDice


class Leader(Character):
    _level = 4
    _size = 0
    _number_abilities = 3
    _base_health = EDice.d10.name
    # Dice type - list contains: 1) Edice 2) number of these Edice
    _dice_type_1 = [EDice.d10, 4]
    _dice_type_2 = [EDice.d8, 2]
    # Dice numbers - list contains: 1) dice numbers 2) numbers of these dice
    _dice_numbers_1 = [3, 4]
    _dice_numbers_2 = [2, 2]
    
    def __init__(self, league, name, health, brawl, shoot, dodge, might,
                 finesse, cunning, **abilities):
        super().__init__(league, name, health, brawl, shoot, dodge,
                           might, finesse, cunning, **abilities)

        results = super().get_skills_input(brawl, shoot, dodge, might,
                                             finesse, cunning)

        super().check_health(health, self._base_health)

        super().check_number_dice(self, results[0])

        super().check_type_dice(self, results[1])

        # Check the abilities which the user has entered
        super().check_abilities( name, self.__class__.__name__, self._level,
                                self._number_abilities, **abilities)

    def __del__(self):
        print(self.__class__.__name__ + " object has been removed.")
