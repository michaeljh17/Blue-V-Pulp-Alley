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

        # Check none of the arguments passed to the function are empty or
        #  missed out
        """ Handle empty arguments - MS """
        """if (name == NULL):
            try:
                raise InputException("Invalid name input")
            except InputException:
                print(name" is not a valid entry for the character name.")"""
        # Could call an exception to check this - would have to be called in
        # the controller - ?
        # check_empty_arg() could be called for each argument. This would
        # enable the system to identify which attributes
        # are missing, if any are missing
        """if not self.check_empty_arg(name, health, brawl, shoot, dodge, might,
                                    finesse, cunning, **abilities):
            return"""

        # Checking the abilities which the user may have attempted to add to
        # the character actually are abilities which
        # are recognised by the system
        # This functionality could be replaced by an exception ...
        # if not self.check_abilities(abilities):
        #    print("Character creation of " + name + " has been unsuccessful, "
        #                                            "please try again.")
        #    return None

        # Check that the character class string the user has entered matches a
        # valid character class
        # if not self.check_valid_character(char_type):
        #    return

        # There needs to be a check that only one Leader and one Side-Kick can
        # be in the league

        # Check that the user has entered valid values for the new character's
        # health
        # if not self.check_health_input(char_type, health):
        #    return

        # Check that the details for the skills which the user has inputted are
        # valid
        # if not self.check_skills_input(char_type, brawl, shoot, dodge, might,
        #                               finesse, cunning):
        #    return

        # There could be a check here that the character is being given a
        # ability with a permitted level, instead of
        # being done after the character creation block

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
        #***Check that adding the character does not exceed the number of slots remaining for the league - MS

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
                new_character = SideKick(self, name, health, brawl, shoot, dodge,
                                         might, finesse, cunning, **abilities)
            elif char_type == Follower.__name__:
                new_character = Follower(self, name, health, brawl, shoot, dodge,
                                         might, finesse, cunning, **abilities)

            # Deduct points from the max total:
            # self._max_points -= new_character.get_subclass_size(
            # new_character) Or:

            if self._max_points < new_character.get_size():
                raise CharacterException("There are not enough league points "
                                         "left to add " +
                                         new_character.get_name() + " the " +
                                         new_character.__class__.__name__ +
                                         " to the league.")
            else:
                self._max_points -= new_character.get_size()
            '''
            print("Character creation of " + name + " the " + char_type +
                  " has been successful!")'''
            self._all_my_characters.append(new_character)
            '''
            print("League points remaining: " + str(self._max_points))'''
            return new_character

        except CharacterException as e:
            print(e.value)
            del new_character

        # These commented out checks are now performed before the character
        # creation:
        # if not self.check_number_skill_dice(new_character):
        #    return print("Character creation of " + name + " the " + char_type
        #  + " has been unsuccessful, please try
        # again.")

        # if not self.check_type_skill_dice(new_character):
        #    return print("Character creation of " + name + " the " + char_type
        #  + " has been unsuccessful, please try
        # again.")

        """if not self.check_number_abilities(new_character):
            print("Character creation of " + name + " the " + char_type +
                  " has been unsuccessful, please try again.")
            return

        errors_level = False
        errors_dupl = False

        for ability in new_character.get_abilities():
            print("Ability to be added: " + ability.get_name())
            print("Ability level: " + ability.get_level())

            # The level value of each ability object needs to be converted into
            #  a int - because the
            # instances of Ability have been obtained from file Strings
            if not self.check_level_abili(new_character,
                                          int(ability.get_level())):
                errors_level = True

            # If none of the character's abilities are duplicates then the
            # character is okay
            if self.check_duplicate_values(new_character.get_abilities()):
                errors_dupl = True

        if errors_level:
            print("Character creation of " + name + " the " + char_type +
                  " has been unsuccessful, please try again.")
            return

        if errors_dupl:
            print("User has tried to give the character a duplicate ability")
            print("Character creation has been unsuccessful, please try "
                  "again.")
            return

        print("Character creation of " + name + " the " + char_type +
              " has been successful!")
        self._all_my_characters.append(new_character)
        return new_character"""

    def delete_character_by_name(self, characterName):
        count = 0
        the_character = self.find_character(characterName)
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

    def remove_character(self, char):
        for character in self._all_my_characters:
            if character.get_name() == char.get_name():
                print(
                    character.get_name() +
                    " Deleted // Change my output to view class. ")
                self._all_my_characters.remove(character)
                self._max_points += char.get_size()
                print("League points: " + str(self._max_points))

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
        #print(output)
        return output

# if __name__ == "__main__":
#   import doctest
#   doctest.testmod()

