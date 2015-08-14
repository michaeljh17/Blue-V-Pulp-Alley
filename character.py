__author__ = 'User'

from abc import ABCMeta
from skill import Skill
from eskill import ESkill
from edice import EDice
from input_exception import InputException


class Character(metaclass=ABCMeta):
    """The Character class"""
    __metaclass__ = ABCMeta

    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, **abilities):
        self.__my_league = league
        self.__name = name
        self.__health = self.set_skill(ESkill.health, health)
        self.__brawl = self.set_skill(ESkill.brawl, brawl)
        self.__shoot = self.set_skill(ESkill.shoot, shoot)
        self.__dodge = self.set_skill(ESkill.dodge, dodge)
        self.__might = self.set_skill(ESkill.might, might)
        self.__finesse = self.set_skill(ESkill.finesse, finesse)
        self.__cunning = self.set_skill(ESkill.cunning, cunning)
        self.__abilities = self.set_abilities(**abilities)
        self.__ability_1 = self.__abilities[0]
        # Could use exception handling instead of the if statement when setting ability 2 or 3
        # (in case self.__abilities has only one item in it
        if len(self.__abilities) == 2:
            self.__ability_2 = self.__abilities[1]
        elif len(self.__abilities) == 3:
            self.__ability_3 = self.__abilities[2]

    def __str__(self):
        return self.__name

    @staticmethod
    def set_health(health):
        bool_test = False
        for dice in EDice:
            if health == dice.name:
                return dice

        if not bool_test:
            try:
                raise InputException("Invalid health input")
            except InputException as e:
                print(e.value)

    @staticmethod
    def set_skill(skill_type, skill_input):
        """
        :param skill_type: Type of skill which the user would like to add, as a string
        :param skill_input: The number of dice, and the type of die, of the skill to be set, as a string
        :return:
        """
        number_dice = []
        alpha_array = []
        i = 0
        while i < len(skill_input):
            if skill_input[i].isdigit():
                number_dice.append(skill_input[i])
                i += 1
            elif skill_input[i].isalpha():
                j = 0
                while j < len(skill_input):
                    if skill_input[j].isalpha():
                        alpha_array.append(j)
                        # print(alphaArray[len(alphaArray) - 1])
                    j += 1
                break

        # The following lines will get the number of dice, the type of dice, and the skill type:
        number_dice_str = "".join(number_dice)

        if len(alpha_array) == 0:
            return
        elif len(alpha_array) == 1:
            type_dice_str = skill_input[alpha_array[0]:]
        elif len(alpha_array) > 1:
            type_dice_str = skill_input[alpha_array[0]:alpha_array[1]]

        # When passing the dice-type to the Skill constructor, it should be an EDice type instead of just a string
        type_dice = ""
        for x in EDice:
            if type_dice_str == x.name:
                type_dice = x

        if type_dice == "":
            try:
                raise InputException("User has entered the wrong type of dice")
            except InputException as e:
                print(e.value)
            finally:
                return
        else:
            if skill_type == ESkill.health:
                # print("Adding a health skill")
                return Skill(ESkill.health, type_dice, number_dice_str)
            elif skill_type == ESkill.brawl:
                return Skill(ESkill.brawl, type_dice, number_dice_str)
            elif skill_type == ESkill.shoot:
                return Skill(ESkill.shoot, type_dice, number_dice_str)
            elif skill_type == ESkill.dodge:
                return Skill(ESkill.dodge, type_dice, number_dice_str)
            elif skill_type == ESkill.might:
                return Skill(ESkill.might, type_dice, number_dice_str)
            elif skill_type == ESkill.finesse:
                return Skill(ESkill.finesse, type_dice, number_dice_str)
            elif skill_type == ESkill.cunning:
                return Skill(ESkill.cunning, type_dice, number_dice_str)
            else:
                # An if statement would suffice instead of using and raising exceptions in this manner
                # Just experimenting with exceptions here and elsewhere
                try:
                    raise InputException("'" + skill_type + "' is an unknown skill type")
                except InputException as e:
                    print(e.value)

    def set_abilities(self, **abilities):
        """
        This is a function to set the abilities of a character
        :param abilities: A dictionary of strings of the names of abilities. The keys are: 'arg1', 'arg2', 'arg3'
        :return: A list of Ability objects (unless no valid ability names have been passed to this method)
        """
        abil_coll = self.__my_league.get_my_league_model().get_all_abilities()
        new_abilities = []

        # abilities is a dictionary ? yes
        for new_ab in abilities:
            for existing_ab in abil_coll:
                if abilities[new_ab] == existing_ab.get_name():
                    new_abilities.append(existing_ab)
                    break

        return new_abilities

    def remove_ability(self, ability_name):
        """
        This function will attempt to remove an ability from the character's abilities list
        :param ability_name: the String name of an ability the user would like to remove
        :return: A boolean value to indicate whether the removal has been successful or not
        """
        for ability in self.__abilities:
            if ability.get_name() == ability_name:
                self.__abilities.remove(ability)
                return True
        return False

    def add_ability(self, ability):
        self.__abilities.append(ability)

    def set_ability_1(self, ab_1):
        self.__ability_1 = ab_1

    def set_ability_2(self, ab_2):
        self.__ability_2 = ab_2

    def set_ability_3(self, ab_3):
        self.__ability_3 = ab_3

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_brawl(self):
        return self.__brawl

    def get_dodge(self):
        return self.__dodge

    def get_might(self):
        return self.__might

    def get_shoot(self):
        return self.__shoot

    def get_finesse(self):
        return self.__finesse

    def get_cunning(self):
        return self.__cunning

    def get_name(self):
        return self.__name

    def get_my_league(self):
        return self.__my_league

    def get_abilities(self):
        return self.__abilities

    def get_ability_1(self):
        return self.__ability_1

    def get_ability_2(self):
        return self.__ability_2

    def get_ability_3(self):
        return self.__ability_3

# What does this actually do?
# Character.register(Ally)
