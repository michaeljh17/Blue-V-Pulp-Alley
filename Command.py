# __author__ = 'gazza'
import os
import cmd
import pickle
from league_model import LeagueModel
from input_view import InputView
from input_exception import InputException
from character_exception import CharacterException
from ViewModel.ViewModel import ViewModel
from FilerModule.FilerModule import FilerModule
from skill import Skill
from eskill import ESkill
from character import Character


class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>>"
        self.intro = "Welcome to Python Alley (to view help type 'help')"
        self._lm = LeagueModel()
        self._vm = ViewModel()
        self._fm = FilerModule()

    # Commands are below

    def do_exit(self, args):
        'Exits the program'
        return -1

    def do_createLeague(self, args):
        '''createLeague [LeagueName]
        This command creates a league with the given name.
        '''
        try:
            self._lm.set_abilities_file(self._fm.read_file("abilities.txt"))
            # change to handle file systems
            if args != "":
                self._lm.add_league(args)
                print(args + " created")
            else:
                print("The new league must have a name!")
        except TypeError as e:
            print("Please check your filesystem has all the necessary files.")

    def do_renameLeague(self, args):
        """
        renameLeague [new league name]

        This command allows you to change the name of the current league.

        """
        if self._lm.get_current_league() == "":
            print("You need to create a league first before trying to rename "
                  "a league.")
            return

        if args == "":
            self._vm.display("You must type a new name to replace the old")
        else:
            try:
                self._lm.get_current_league().set_name(args)
            except AttributeError:
                self._vm.display("There is no league to rename. I suggest " +
                                "you create one")
                return
            except Exception as e:
                self._vm.display("You may not rename the league. " + str(e))
                return
        self._vm.display("The league is now named: " +
                        self._lm.get_current_league().get_name())

    def do_deleteLeague(self, args):
        '''
        deleteLeague
        This command will delete the league.
        '''
        if self._lm.get_current_league() == "":
            print("There is no league to be deleted.")
            return

        try:
            current_league_name = str(self._lm.get_current_league())
        except AttributeError:
            print("You do not have a league to delete")
            return

        """
        self.vm.display("You are about to delete the league, " +
                        current_league_name + ". Are you sure you wish to "
                        + "do this? Press Y to delete and N to cancel")
        print(ord('Y'))
        while True:
            key = ord(getch())
            if key == '121' or key == '89':
                self.lm.delete_league()
                self.vm.display(current_league_name + " deleted!")
                break
            else:
                self.vm.display("Your league has not been deleted")
                break
        """
        self._lm.delete_league()
        self._vm.display(current_league_name + " deleted!")

    def do_displayLeague(self, args):
        '''
        displayLeague
        This command will display your current league. It will list the
        current characters and their skills
        '''
        if self._lm.get_current_league() == "":
            print("You need to create a league first before trying to display "
                  "a league.")
            return

        self._vm.display(self._lm.get_current_league())
        self._vm.display(self._vm.build_table(self._lm.export_league()))

    def do_addCharacter(self, args):
        '''
        addCharacter [CharacterName] [CharacterType] [Health] [Brawl] [Shoot]
        [Dodge] [Might] [Finesse] [Cunning]
        [Ability 1] [Ability 2] [Ability 3]
        -----------------------------------------------------------------------
        This command adds a character to the current league.
        Your league starts with 10 roster slots.
        -----------------------------------------------------------------------
        [Character Name] = The character's name
        [CharacterType] = Can be either 'Leader' 'SideKick' 'Ally' or
        'Follower', You can only have ONE leader

        Skills. See below for examples on how to use this argument

        [Health] = A number used to represent your characters overall condition
        [Brawl] = Represents a character's overall hand-to-hand combat prowess
        [Shoot] = Indicates a character's combat effectiveness with all manner
                  of ranged weapons
        [Dodge] = Determines the character's ability to avoid enemy attacks,
                  perils, and other dangers.
        [Might] = Indicates a character's power, fitness and general
                  athleticism
        [Finesse] = measures the character's co ordination, awareness and
                  ability to manipulate
        [Cunning] = Represents a character's knowledge, resolve and ability to
                  solve complicated problems.

        Skill levels by type

        Leader
            MUST have a health value of d10
            Select four skills to start at 3 dice and two skills to start at
            2 dice
            Select four skills to start at d10 and two skills to start at d8
            Can choose 3 abilities at any level
        SideKick
            MUST have a health value of d8
            Select three skills to start at 3 dice and three skills to start at
            2 dice
            Select three skills to start at d8 and three skills to start at d6
            Can choose 2 abilities at level 1 to 3
            Uses three roster slots
        Ally
            MUST have a health value of d6
            Select two skills to start at 2 dice and four skills to start at
            1 dice
            All skills start at d6
            Can choose 1 ability at level 1 to 2
            Uses two roster slots
        Follower
            MUST have a health value of d6
            ALL skills must be 1d6
            Can choose 1 ability at level 1
            Uses one roster slot

        Example
            addCharacter Testing Leader d10 3d8 3d10 3d10 2d8 3d10 2d10 Mighty
            Brash Crafty
        '''
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before adding a "
                  "character.")
            return

        result = args.split(" ")
        inputV = InputView()

        if self._lm.get_current_league() is None:
            print("You need to create a league first!")
            return

        if len(result) >= 10:
            try:
                inputV.check_valid_name(result[0])
                inputV.check_valid_class(result[1])
                inputV.check_valid_skill_dice(result[3])
                inputV.check_valid_skill_dice(result[4])
                inputV.check_valid_skill_dice(result[5])
                inputV.check_valid_skill_dice(result[6])
                inputV.check_valid_skill_dice(result[7])
                inputV.check_valid_skill_dice(result[8])

                if len(result) == 10:
                    try:
                        inputV.check_valid_ability(result[9],
                                                   self._lm.get_all_abilities())
                        league.add_character(name=result[0],
                                             char_type=result[1],
                                             health=result[2], brawl=result[3],
                                             shoot=result[4], dodge=result[5],
                                             might=result[
                                                 6], finesse=result[7],
                                             cunning=result[8], arg1=result[9])
                    except InputException as e:
                        print(e.value)

                elif len(result) == 11:
                    try:
                        inputV.check_valid_ability(result[9],
                                                   self._lm.get_all_abilities())
                        inputV.check_valid_ability(result[10],
                                                   self._lm.get_all_abilities())
                        inputV.check_duplicate_values(result[9], result[10])

                        league.add_character(name=result[0],
                                             char_type=result[1],
                                             health=result[2], brawl=result[3],
                                             shoot=result[4], dodge=result[5],
                                             might=result[6],
                                             finesse=result[7],
                                             cunning=result[8], arg1=result[9],
                                             arg2=result[10])
                    except InputException as e:
                        print(e.value)

                elif len(result) == 12:
                    try:
                        inputV.check_valid_ability(result[9],
                                                   self._lm.get_all_abilities())
                        inputV.check_valid_ability(result[10],
                                                   self._lm.get_all_abilities())
                        inputV.check_valid_ability(result[11],
                                                   self._lm.get_all_abilities())
                        inputV.check_duplicate_values(result[9], result[10],
                                                      result[11])
                        league.add_character(name=result[0],
                                             char_type=result[1],
                                             health=result[2], brawl=result[3],
                                             shoot=result[4], dodge=result[5],
                                             might=result[
                                                 6], finesse=result[7],
                                             cunning=result[8], arg1=result[9],
                                             arg2=result[10], arg3=result[11])
                    except InputException as e:
                        print(e.value)
                else:
                    print("You have entered too many arguments. Please try "
                          "again.")
            except InputException as e:
                print(e.value)
        else:
            print("You have not entered enough arguments to create a character"
                  ". Please try again.")

    def do_rename_character(self, args):
        '''
        rename_character [oldName] [newName]

        Renames the character with a new name provided
        Names must be one word with no spaces
        '''
        # > Error handling: need to check that the character exists in league
        # > Error handling: need to check that the new name is not an empty
        # string
        result = args.split(" ")
        # self.vm.display("Results: " + result[0] + " " + result[1])
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before trying to rename "
                  "one of its characters.")
            return

        character = league.find_character(result[0])
        # try:
        character.set_name(result[1])
        # except
        self._vm.display(result[0] + " has been renamed to " +
                        character.get_name())

    def do_delete_character(self, args):
        '''
        delete_character [Character Name]

        This command will delete the character
        '''
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before trying to delete "
                  "one of its characters.")
            return

        character = league.find_character(args)
        if character is not None:
            league.remove_character(character)
        else:
            self._vm.display("'" + args + "' is not recorded as being in the "
                                          "league. No character has been "
                                          "deleted.")

    def do_replace_ability(self, args):
        '''
        replace_ability [Character Name] [Old Ability] [New Ability]

        Replaces an ability on a character
        '''
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before trying to "
                  "replace the ability of one of its characters.")
            return

        result = args.split(" ")
        if len(result) < 3:
            print("Not enough arguments. Please try again")
            return
            # What if there are too many arguments ???

        input_v = InputView()
        character = league.find_character(result[0])

        if character is not None:
            try:
                input_v.check_valid_ability(result[1],
                                            self._lm.get_all_abilities())
                input_v.check_valid_ability(result[2],
                                            self._lm.get_all_abilities())
                character.replace_ability(character, result[1], result[2])
                # print(result[0] + " has had the ability " + result[1] +
                #      " replaced with " + result[2])
            except InputException as e:
                print(e.value)
        else:
            print(result[0] + " is not in the " +
                  self._lm.get_current_league().get_name() + " league Please "
                                                             "try again.")

    # Two methods for replacing all of a character's abilities:

    def do_replace_all_abilities(self, args):
        '''
        replace_all_abilities [Character Name] [new ability1] [new ability 2]
        [new ability 3]

        Replaces all abilities on a character
        '''
        result = args.split(" ")
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before trying to "
                  "replace the abilities of one of its characters.")
            return

        character = league.find_character(result[0])

        # Error handling:
        if character is not None:
            self.replace_all_abilities(result, character)
        else:
            print(
                "Please include the name of a character who is in the league")

    def replace_all_abilities(self, result, character):
        """
        Written by MH
        This method will check whether the character's abilities can be
        replaced with new ones
        :param result: a list con
        :param character:
        :return:
        """
        input_v = InputView()

        if len(result) == 1:
            print("You have not set any abilities")
        elif len(result) == 2:
            try:
                # Validate the input:
                input_v.check_valid_ability(result[1],
                                            self._lm.get_all_abilities())
                character.check_abilities(character.get_name(),
                                          character.__class__.__name__,
                                          character.get_subclass_level
                                          (character),
                                          character.get_number_abilities(),
                                          arg1=result[1])

                # Delete the character's current abilities and set the new ones
                character.clear_abilities()
                character.set_abilities(arg1=result[1])
                print("New abilities have been set for " +
                      character.get_name() + ": " +
                      character.get_abilities()[0].get_name())
            except InputException as e:
                print(e.value)
            except CharacterException as e:
                print(e.value)

        elif len(result) == 3:
            try:
                # Validate the input:
                input_v.check_valid_ability(result[1],
                                            self._lm.get_all_abilities())
                input_v.check_valid_ability(result[2],
                                            self._lm.get_all_abilities())
                character.check_abilities(character.get_name(),
                                          character.__class__.__name__,
                                          character.get_subclass_level
                                          (character),
                                          character.get_number_abilities(),
                                          arg1=result[1], arg2=result[2])

                # Delete the character's current abilities and set the new ones
                character.clear_abilities()
                character.set_abilities(arg1=result[1], arg2=result[2])
                print("New abilities have been set for " +
                      character.get_name() + ": " +
                      character.get_abilities()[0].get_name() + " " +
                      character.get_abilities()[1].get_name())
            except InputException as e:
                print(e.value)
            except CharacterException as e:
                print(e.value)

        elif len(result) == 4:
            try:
                # Validate the input:
                input_v.check_valid_ability(result[1],
                                            self._lm.get_all_abilities())
                input_v.check_valid_ability(result[2],
                                            self._lm.get_all_abilities())
                input_v.check_valid_ability(result[3],
                                            self._lm.get_all_abilities())
                character.check_abilities(character.get_name(),
                                          character.__class__.__name__,
                                          character.get_subclass_level
                                          (character),
                                          character.get_number_abilities(),
                                          arg1=result[1], arg2=result[2],
                                          arg3=result[3])

                # Delete the character's current abilities and set the new ones
                character.clear_abilities()
                character.set_abilities(arg1=result[1], arg2=result[2],
                                        arg3=result[3])
                print("New abilities have been set for " +
                      character.get_name() + ": " +
                      character.get_abilities()[0].get_name() + " " +
                      character.get_abilities()[1].get_name() + " " +
                      character.get_abilities()[2].get_name())
            except InputException as e:
                print(e.value)
            except CharacterException as e:
                print(e.value)
        else:
            print("You have entered too many arguments. Please try again.")

    # Three methods involved in editing a character's skills:

    def do_edit_skills(self, args):
        """
        edit_skills [Character Name] [Brawl] [Shoot] [Dodge] [Might] [Finesse]
        [Cunning]

        Edits the value for the skills for a character
        """
        result = args.split(" ")
        league = self._lm.get_current_league()
        if league == "":
            print("You need to create a league first before trying to "
                  "replace the abilities of one of its characters.")
            return

        character = league.find_character(result[0])

        if character is not None:
            self.edit_skills_middle(result, character)
        else:
            print("Invalid character name entered. Please try again.")

    def edit_skills_middle(self, result, character):
        """
        Written by MH
        This function will continue the process of checking whether a
        character's skills can be modified
        :param result: a list containing the user's input
        :param character: the instance of character
        :return:
        """
        if len(result) == 7:
            self.edit_skills_last(result, character)
        else:
            print("You have not entered enough data for all of the skills. "
                  "Please try again")

    def edit_skills_last(self, result, character):
        """
        Written by MH
        This function is the final method which checks whether a
        character's skills can be modified
        :param result: a list containing the user's input
        :param character: the instance of character
        :return:
        """
        input_v = InputView()

        try:
            input_v.check_valid_skill_dice(result[1])
            input_v.check_valid_skill_dice(result[2])
            input_v.check_valid_skill_dice(result[3])
            input_v.check_valid_skill_dice(result[4])
            input_v.check_valid_skill_dice(result[5])
            input_v.check_valid_skill_dice(result[6])

            # Start with the first skill input data, not the name:
            # remove the character name from the results list
            # The result list will now be length 6
            del result[0]

            # Get the skills data from each of the args
            num_dice_list = []
            type_dice_list = []

            for i in range(len(result)):
                dice_str_data = \
                    Character.obtain_dice_data(result[i])
                # print("number_dice_str: "+ number_dice_str)
                # print("type_dice_str: " + type_dice_str)
                num_dice_list.append(dice_str_data[0])
                type_dice_list.append(dice_str_data[1])

            try:
                character.check_number_dice(character, num_dice_list)

                try:
                    character.check_type_dice(character, type_dice_list)

                    # If the previous tests pass then the original skills
                    # can be removed and replaced with the updated skills:

                    skills_result = Character.obtain_dice_data(
                        result[0])
                    character.set_brawl(Skill(ESkill.brawl,
                                              character.find_edice
                                              (skills_result[1]),
                                              skills_result[0]))

                    skills_result = Character.obtain_dice_data(
                        result[1])
                    character.set_shoot(Skill(ESkill.shoot,
                                              character.find_edice
                                              (skills_result[1]),
                                              skills_result[0]))

                    skills_result = Character.obtain_dice_data(
                        result[2])
                    character.set_dodge(Skill(ESkill.dodge,
                                              character.find_edice
                                              (skills_result[1]),
                                              skills_result[0]))

                    skills_result = Character.obtain_dice_data(
                        result[3])
                    character.set_might(Skill(ESkill.might,
                                              character.find_edice
                                              (skills_result[1]),
                                              skills_result[0]))

                    skills_result = Character.obtain_dice_data(
                        result[4])
                    character.set_finesse(Skill(ESkill.finesse,
                                                character.find_edice
                                                (skills_result[1]),
                                                skills_result[0]))

                    skills_result = Character.obtain_dice_data(
                        result[5])
                    character.set_cunning(Skill(ESkill.cunning,
                                                character.find_edice
                                                (skills_result[1]),
                                                skills_result[0]))

                    print(character.get_name() + "'s skills have "
                                                 "successfuly been "
                                                 "replaced.")
                except CharacterException as e:
                    print(e.value)
            except CharacterException as e:
                print(e.value)
        except InputException as e:
            print(e.value)

    def do_display_character(self, args):
        '''
        display_character [Character Name]

        Example:
        display_character Fred

        Displays all information for a given character
        '''
        if self._lm.get_current_league() == "":
            print("You need to create a league first before trying to "
                  "view a character in a league.")
            return

        if args == "" or args is None:
            print("You must type the name of the character you wish to " +
                  "display")
        else:
            try:
                result = self._vm.build_character_table(
                    self._lm.export_character(args))
                self._vm.display(result)

            except:
                print("Unable to find that character, Are you sure they " +
                      "exist?")

    def do_import(self, args):
        '''
        import
        import [file location] [file name]
        
        Imports a file from a specified location and loads it, when no arguments are supplied is uses a default file
        written by Sean
        '''
        
        result = args.split(" ")
        looks_good = False

        if args == "":
            looks_good = True
            self._lm = self._fm.import_binary_league()
        if len(result) == 2:
            looks_good = True
            self._lm = self._fm.import_binary_league(result[0], result[1])
        
        

        if looks_good:
            if self._lm != None:
                self.do_displayLeague(None)
            else:
                self._lm = LeagueModel()                
                self._vm.display("Filepath incorrect, please try again")
        else:
            self._vm.display("Incorrect syntax:" + "\r" + "import [file location] [file name]")
            

    def do_save(self, args):
        '''
        save [file location] [file name]

        Saves a file for the game, prepares it for import in future. If no arguments present, default file is used
        written by Sean
        '''
        if self._lm.get_current_league() == "":
            print("No league to save. Please load or create a league first.")
            return

        result = args.split(" ")
        if args == "":
            print("no args")
            self._fm.export_league_binary_to_fs(self._lm)
        if len(result) == 2:                    
            self._fm.export_league_binary_to_fs(self._lm,result[0],result[1])


    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        In that case we execute the line as Python code.
        """
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print(e.__class__, ":", e)

if __name__ == '__main__':
    console = Console()
    console.cmdloop()
