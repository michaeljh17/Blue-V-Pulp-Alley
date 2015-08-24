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

        # First need to check that the user has not created a character with
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
            if char_type == Leader.__name__:
                new_character = Leader(self, name, health, brawl, shoot, dodge,
                                       might, finesse, cunning, **abilities)
            elif char_type == Ally.__name__:
                new_character = Ally(self, name, health, brawl, shoot, dodge,
                                     might, finesse, cunning, **abilities)
            elif char_type == SideKick.__name__:
                new_character = SideKick(self, name, health, brawl, shoot,
                                         dodge, might, finesse, cunning,
                                         **abilities)
            elif char_type == Follower.__name__:
                new_character = Follower(self, name, health, brawl, shoot,
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
                return
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
        # -MS-
        # find the character object using the name as a given reference
        character = self.find_character(character_name)
        character_data = character.export_character()
        # create a 3D array
        result = []
        first_row = []
        second_row = []
        third_row = []
        fourth_row = []
        # First row array is to contain - Name
        first_row.append(["Name", character_data[1]])
        result.append(first_row)
        # Second row array is to contain - Type
        second_row.append(["Type", character_data[0]])
        result.append(second_row)
        # Third row array is to contain - Skills
        third_row.append(["Skills"])
        third_row.append(
            ["Health", "Brawl", "Shoot", "Dodge", "Might", "Finesse",
             "Cunning"])
        third_row.append([character_data[2], character_data[3],
                          character_data[4],
                          character_data[5], character_data[
                              6], character_data[7],
                          character_data[8]])
        result.append(third_row)
        # Fourth row array is to contain - abilities
        fourth_row.append(["Abilities"])
        fourth_row.append([character_data[9]])
        result.append(fourth_row)

        # return an array of the character's attributes
        return result
