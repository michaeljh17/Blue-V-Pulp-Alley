__author__ = 'gazza'
import os
import cmd
from league_model import LeagueModel
from input_view import InputView
from input_exception import InputException
from ViewModel.ViewModel import ViewModel
from league import League
from character import Character
import sys

class Console(cmd.Cmd):


    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>>"
        self.intro = "Welcome to Burger King, Please place your order"
        self.lm = LeagueModel()
        self.vm = ViewModel()

    ## Commands are below

    def do_exit(self, args):
        'Exits the program'
        return -1

    def do_createLeague(self,args):
        '''createLeague [LeagueName]
        This command creates a league with the given name.
        > Error handling: need to make sure that the new league is not given
        an empty string as a name
        '''
        self.lm.set_abilities_file(self.lm.read_file("abilities.txt")) #change to handle file systems
        if args != "":
            self.lm.add_league(args)
            print(args + " created")
        else:
            print("The new league must have a name!")

    def do_deleteLeague(self,args):
        '''
        deleteLeague [LeagueName]
        This command will delete you specify with a league name
        '''
        print("League deleted (Not actually shhhh)")

    def do_displayLeague(self,args):
        '''
        displayLeague
        This command will display ???
        '''
        print("Leagues go here")
        self.vm.display("Leagues go here")
        self.vm.display(self.vm.build_table(self.lm.export_league()))

    def do_displayAbilities(self,args):
        '''
        displayAbilities
        This command will display all the abilities of the current league
        '''
        ##Output for displaying abilities here

    def do_addCharacter(self,args):
        '''
        addCharacter [CharacterName] [CharacterType] [Health] [Brawl] [Shoot] [Dodge] [Might] [Finesse] [Cunning]
        [Ability 1] [Ability 2] [Ability 3]
        --------------------------------------------------------------------------------------------------------
        This command adds a character to the current league.
        Your league starts with 10 roster slots.
        --------------------------------------------------------------------------------------------------------
        [Character Name] = The character's name
        [CharacterType] = Can be either 'Leader' 'SideKick' 'Ally' or 'Follower', You can only have ONE leader

        Skills. See below for examples on how to use this argument

        [Health] = A number used to represent your characters overall condition
        [Brawl] = Represents a character's overall hand-to-hand combat prowess
        [Shoot] = Indicates a character's combat effectiveness with all manner of ranged weapons
        [Dodge] = Determines the character's ability to avoid enemy attacks, perils, and other dangers.
        [Might] = Indicates a character's power, fitness and general athleticism
        [Finesse] = measures the character's co ordination, awareness and ability to manipulate
        [Cunning] = Represents a character's knowledge, resolve and ability to solve complicated problems.

        Skill levels by type

        Leader
            MUST have a health value of d10
            Select four skills to start at 3 dice and two skills to start at 2 dice
            Select four skills to start at d10 and two skills to start at d8
            Can choose 3 abilities at any level
        SideKick
            MUST have a health value of d8
            Select three skills to start at 3 dice and three skills to start at 2 dice
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
        league = self.lm.get_current_league()
        result = args.split(" ")
        inputV = InputView()

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
                                                   self.lm.get_all_abilities())
                        league.add_character(name=result[0],char_type=result[1],
                                             health=result[2],brawl=result[3],
                                             shoot=result[4],dodge=result[5],
                                             might=result[6],finesse=result[7],
                                             cunning=result[8],arg1=result[9])
                    except InputException as e:
                        print(e.value)

                elif len(result) == 11:
                    try:
                        inputV.check_valid_ability(result[9],
                                                   self.lm.get_all_abilities())
                        inputV.check_valid_ability(result[10],
                                                   self.lm.get_all_abilities())
                        inputV.check_duplicate_values(result[9], result[10])

                        league.add_character(name=result[0],char_type=result[1],
                                             health=result[2],brawl=result[3],
                                             shoot=result[4],dodge=result[5],
                                             might=result[6], finesse=result[7],
                                             cunning=result[8],arg1=result[9],
                                             arg2=result[10])
                    except InputException as e:
                        print(e.value)

                elif len(result) == 12:
                    try:
                        inputV.check_valid_ability(result[9],
                                                   self.lm.get_all_abilities())
                        inputV.check_valid_ability(result[10],
                                                   self.lm.get_all_abilities())
                        inputV.check_valid_ability(result[11],
                                                   self.lm.get_all_abilities())
                        inputV.check_duplicate_values(result[9], result[10],
                                                      result[11])
                        league.add_character(name=result[0],char_type=result[1],
                                             health=result[2],brawl=result[3],
                                             shoot=result[4],dodge=result[5],
                                             might=result[6],finesse=result[7],
                                             cunning=result[8],arg1=result[9],
                                             arg2=result[10], arg3=result[11])
                    except InputException as e:
                        print(e.value)

            except InputException as e:
                print(e.value)
        else:
            print("You have not entered enough arguments to create a character "
                  "Please try again.")

    def do_rename_character(self,args):
        '''
        rename_character [oldName] [newName]
        Renames the character with a new name provided
        Names must be one word with no spaces
        > Error handling: need to check that the character exists in league
        > Error handling: need to check that the new name is not an empty string
        '''
        result = args.split(" ")
        print("Results: " + result[0] + " " + result[1])
        league = self.lm.get_current_league()
        character = league.find_character(result[0])
        # try:
        character.set_name(result[1])
        # except
        print(result[0] + " has been renamed to " + character.get_name())

    def do_delete_character(self,args):
        '''
        delete_character [Character Name]

        This command will delete the character
        '''
        league = self.lm.get_current_league()
        character = league.find_character(args)
        league.remove_character(character)

    def do_replace_ability(self,args):
        '''
        replace_ability [Character Name] [Old Ability] [New Ability]

        Replaces an ability on a character
        '''
        result = args.split(" ")
        if len(result) < 3:
            print("Not enough arguments. Please try again")
            # What if there are too many arguments ???
            return
        inputV = InputView()
        league = self.lm.get_current_league()
        # character = ""

        character = league.find_character(result[0])
        if character is not None:
            try:
                inputV.check_valid_ability(result[1], self.lm.get_all_abilities())
                inputV.check_valid_ability(result[2], self.lm.get_all_abilities())
                character.replace_ability(character, result[1] ,result[2])
                print(result[0] + " has had the ability " + result[1] + " replaced "
                                                                        "with " +
                      result[2])
            except InputException as e:
                print(e.value)
        else:
            print("Invaid character name entered. Please try again.")

    def do_replace_all_abilities(self,args):
        '''
        replace_all_abilities [Character Name] [new ability1] [new ability 2] [new ability 3]

        Replaces all abilities on a character
        '''
        result = args.split(" ")
        league = self.lm.get_current_league()
        character = league.find_character(result[0])
        if len(result) == 0:
            print("You have not set any abilities")
        if len(result) == 1:
            character.set_abilities(arg1 = result[1])
        if len(result) == 2:
            character.set_abilities(arg1 = result[1], arg2 = result[2])
        if len(result) == 3:
            character.set_abilities(arg1 = result[1], arg2 = result[2],
                                    arg3 = result[3])

    def do_edit_skills(self,args):
        '''
        edit_skills [Character Name] [Brawl] [Shoot] [Dodge] [Might] [Finesse] [Cunning]

        Edits the value for the skills for a character
        '''

    def do_display_character(self,args):
        '''
        display_character [Character Name]

        Displays all information for a character
        '''

    def do_import(self,args):
        '''
        import [file location] [file name]

        Imports a file from a specified location and loads it
        '''

    def do_save(self,args):
        '''
        save [file location] [file name]

        Saves a file for the game, prepares it for import in future
        '''

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        In that case we execute the line as Python code.
        """
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print (e.__class__, ":", e)

if __name__ == '__main__':
        console = Console()
        console.cmdloop()