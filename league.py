from input_exception import InputException
from character_exception import CharacterException
from leader import Leader
from side_kick import SideKick
from ally import Ally
from follower import Follower
from edice import EDice
from _overlapped import NULL
from test.test_audioop import INVALID_DATA
from character import Character


class League(object):
    """
    The League class
    """

    def __init__(self, league_model, name, all_my_chars=[], max_points=10):
        self._name = name
        self._all_my_characters = all_my_chars
        self._max_points = max_points
        self._my_league_model = league_model
        self._leader_in_league = False

    def __str__(self):
        return self._name

    def get_all_my_characters(self):
        return self._all_my_characters

    def set_name(self, newName):
        self._name = newName

    def get_name(self):
        return self._name

    def get_my_league_model(self):
        return self._my_league_model

    def find_character(self, char_name):
        for ch in self._all_my_characters:
            if ch.get_name() == char_name:
                return ch
        return None

    def add_character(self, name="", char_type="", health="", brawl="",
                      shoot="", dodge="", might="", finesse="",
                      cunning="", **abilities):
        """
        Adds a new character to the league
        """
        # Preconditions of this method: valid data has been entered by the
        # user: the class and ability names and dice type strings.

        # Need to check whether a leader has been added to the league. If not
        # then unless the new character is the leader, then the user should
        # not be able to add the character to the league:

        try:
            if not self.check_leader(char_type):
                return
        except CharacterException as e:
            print(e)
            return

        # Need to check that the user has not created a character with
        # the same name as an existing character: These 'if not' statements
        # are saying if the result is False then ...

        if not self.check_duplicate_name(name):
            # This is the same as returning None
            return

        # Check that the user has not attempted to add a character that breaks
        # the character member rules - MS
        # May only have one leader.
        # May only have one sidekick unless 'Company of Heroes' perk is
        # chosen
        try:
            self.check_duplicate_type(char_type)
        except CharacterException as e:
            print(e)
            return
        # ***Check that adding the character does not exceed the number of
        # slots remaining for the league - MS

        # If no errors have been found then the characters can be created

        new_character = ""

        try:
            for subChar in Character.__subclasses__():
                if char_type == subChar.__name__:
                    new_character = subChar(self, name, health, brawl, shoot,
                                            dodge, might, finesse, cunning,
                                            **abilities)

            if self._max_points < new_character.get_size():
                raise CharacterException("There are not enough league points "
                                         "left to add " +
                                         new_character.get_name() + " the " +
                                         new_character.__class__.__name__ +
                                         " to the league.")

            else:
                self._max_points -= new_character.get_size()

                print("Character creation of " + name + " the " + char_type +
                      " has been successful")
                self._all_my_characters.append(new_character)
                print("League points remaining: " + str(self._max_points))
                return new_character

        except CharacterException as e:
            print(e.value)
            del new_character

    def delete_character_by_name(self, character_name):
        count = 0
        the_character = self.find_character(character_name)
        for each_character in self._all_my_characters:
            if (the_character == each_character):
                del self._all_my_characters[count]
                count += 1

    @staticmethod
    def check_valid_character(char_type):
        if char_type == Leader.__name__ or char_type == Ally.__name__ or \
            char_type == SideKick.__name__ or char_type \
                == Follower.__name__:
            return True
        else:
            return False

    def check_duplicate_name(self, name):
        for c in self._all_my_characters:
            if name == c.get_name():
                print("The name, " + name + ", is already the name of an "
                                            "existing character. Please try "
                                            "again.")
                return False
        return True

    def check_duplicate_type(self, char_type):
        # -MS-
        # If the new character's type is Leader or Sidekick
        if char_type == 'Leader' or char_type == 'SideKick':
            # Check the leagues current characters to ensure that
            # there isn't already a character of the same type
            for theCharacter in self._all_my_characters:
                # If there is a match, throw exception
                if theCharacter.__class__.__name__ == char_type:
                    raise CharacterException("You may only have one" +
                                             char_type)
            # If there is not a match, continue with the process of
            # adding a new character.

    def remove_character(self, charac):
        for character in self._all_my_characters:
            if charac.__class__.__name__ is not Leader.__name__:
                if character.get_name() == charac.get_name():
                    print(
                        character.get_name() +
                        " Deleted")
                    self._all_my_characters.remove(character)
                    self._max_points += charac.get_size()
                    print("League points: " + str(self._max_points))
            else:
                print("You are not allowed to delete the leader of a league.")

    def export_league(self):
        output = []

        headings_array = []
        headings_array.append("Class")
        headings_array.append("Name")
        headings_array.append("Health")
        headings_array.append("Brawl")
        headings_array.append("Shoot")
        headings_array.append("Dodge")
        headings_array.append("Might")
        headings_array.append("Finesse")
        headings_array.append("Cunning")
        headings_array.append("Abilities")
        output.append(headings_array)

        for character in self._all_my_characters:
            output.append(character.export_character())
        # print(output)
        return output

    def export_character(self, character_name):
        result = []
        new_row = []
        the_character = self.find_character(character_name)
        character_data = the_character.export_character()
        # print("Character data " + str(character_data))
        new_row = [character_data[1]]
        result.append(new_row)
        new_row = ["Type", character_data[0]]
        result.append(new_row)
        new_row = ["Skills"]
        result.append(new_row)
        new_row = ["Health", "Brawl", "Shoot", "Dodge", "Might", "Finesse",
                   "Cunning"]
        result.append(new_row)
        new_row = [character_data[2], character_data[3], character_data[4],
                   character_data[5], character_data[6], character_data[7],
                   character_data[8]]
        result.append(new_row)
        new_row = []
        abilities = [x.strip() for x in character_data[9].split(',')]
        for the_ability in abilities:
            new_row.append(the_ability)
        result.append(new_row)

        # print("Result from league " + str(result))
        return result

    def check_leader(self, char_type):
        """
        This function will raise an exception if the user attempts to add a
        character which is not a leader to a league and the league does not
        yet have a leader
        :param char_type: class of character
        :return: True, unless the exception is raised.
        """
        if self._leader_in_league:
            return True
        else:
            if char_type == "Leader":
                self._leader_in_league = True
                return True
            else:
                raise CharacterException("You must first add a leader to a "
                                         "league before adding any other type "
                                         "of character.")
