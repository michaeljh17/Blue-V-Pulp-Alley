__author__ = 'User'

from abc import ABCMeta
from skill import Skill
from eskill import ESkill
from edice import EDice
from input_exception import InputException


class Character(metaclass=ABCMeta):
    """The Character class"""
    __metaclass__ = ABCMeta

    def __init__(self, name, health="", brawl="", shoot="", dodge="", might="", finesse="", cunning=""):
        self.__name = name
        # self.__char_type = self.set_char_type(char_type)
        self.__health = self.set_skill(ESkill.health, health)
        self.__brawl = self.set_skill(ESkill.brawl, brawl)
        self.__shoot = self.set_skill(ESkill.shoot, shoot)
        self.__dodge = self.set_skill(ESkill.dodge, dodge)
        self.__might = self.set_skill(ESkill.might, might)
        self.__finesse = self.set_skill(ESkill.finesse, finesse)
        self.__cunning = self.set_skill(ESkill.cunning, cunning)

    def get_char_type(self):
        return self.__char_type

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

        # The following will get the number of dice, the type of dice, and the skill type:
        number_dice_str = "".join(number_dice)

        if len(alpha_array) > 1:
            type_dice_str = skill_input[alpha_array[0]:alpha_array[1]]
        else:
            type_dice_str = skill_input[alpha_array[0]:]
        # debugging:
        # skill_t = skill_input[alphaArray[1]:]
        # print(skill_t)
        # print(number_dice_str)
        # print(type_dice_str)

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
                print("Adding a health skill")
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

# What does this actually do?
# Character.register(Ally)
