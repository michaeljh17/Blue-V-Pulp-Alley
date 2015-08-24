__author__ = 'gazza'
import os
import cmd
from league_model import LeagueModel
from league import League
from character import Character
import sys

class Console(cmd.Cmd):

    lm = LeagueModel()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>>"
        self.intro = "Welcome to Burger King, Please place your order"

    ## Commands are below

    def do_exit(self, args):
        'Exits the program'
        return -1

    def do_createLeague(self,args):
        """
        createLeague [LeagueName]
        This command creates a league with the given name.

        >>> Console.do_createLeague(Console,"Test")
        Test created
        """
        self.lm.set_abilities_file(self.lm.read_file("abilities.txt")) #change to handle file systems
        self.lm.add_league(args)
        print(args + " created")

    def do_deleteLeague(self,args):
        '''
        ##Test to be completed

        deleteLeague [LeagueName]
        This command will delete you specify with a league name
        '''
        print("League deleted (Not actually shhhh)")

    def do_displayLeague(self,args):
        '''
        Test to be completed
        displayLeague
        This command will display ???
        '''
        print("Leagues go here")

    def do_displayAbilities(self,args):
        '''
        test to be completed
        displayAbilities
        This command will display all the abilities of the current league
        '''
        #Output for displaying abilities here

    def do_addCharacter(self,args):
        """
        >>> Console.do_createLeague(Console,"Test")
        Test created
        >>> Console.do_addCharacter(Console, "Tester Leader d10 3d10 3d10 3d10 3d10 2d8 2d8 Animal Brash Deadeye")
        Character creation of Tester the Leader has been successful!

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
            Select three skills to start at d10 and three skills to start at d8
            Can choose 2 abilities at level 1 to 3
            Uses three roster slots
        Ally
            MUST have a health value of d6
            Select two skills to start at 3 dice and four skills to start at 2 dice
            All skills start at d6
            Can choose 1 ability at level 1 to 2
            Uses two roster slots
        Follower
            MUST have a health value of d6
            ALL skills must be 1d6
            Can choose 1 ability at level 1
            Uses one roster slot

        Example
            addCharacter Testing Leader d10 3d8 3d10 3d10 2d8 3d10 2d10 Mighty Brash Crafty
        """
        league = self.lm.get_current_league()
        result = args.split(" ")
        if len(result) == 10:
            league.add_character(name=result[0],char_type=result[1],health=result[2],brawl=result[3],shoot=result[4],dodge=result[5],might=result[6],finesse=result[7],cunning=result[8],arg1=result[9])

        if len(result) == 11:
            league.add_character(name=result[0],char_type=result[1],health=result[2],brawl=result[3],shoot=result[4],dodge=result[5],might=result[6],finesse=result[7],cunning=result[8],arg1=result[9], arg2=result[10])

        if len(result) == 12:
            league.add_character(name=result[0],char_type=result[1],health=result[2],brawl=result[3],shoot=result[4],dodge=result[5],might=result[6],finesse=result[7],cunning=result[8],arg1=result[9], arg2=result[10], arg3=result[11])

    def do_rename_character(self,args):
        '''
        >>> Console.do_createLeague(Console,"Test")
        Test created
        >>> Console.do_addCharacter(Console, "Test_rename Leader d10 3d10 3d10 3d10 3d10 2d8 2d8 Animal Brash Deadeye")
        Character creation of Test_rename the Leader has been successful!
        >>> Console.do_rename_character(Console,"Test_rename Testing")
        Test_rename renamed to Testing

        rename_character [oldName] [newName]
        Renames the character with a new name provided
        Names must be one word with no spaces
        '''
        result = args.split(" ")
        league = self.lm.get_current_league()
        character = league.find_character(result[0])
        character.set_name(result[1])
        print(result[0] + " renamed to " + character.get_name())

    def do_delete_character(self,args):
        """
        >>> Console.do_createLeague(Console,"Test")
        Test created
        >>> Console.do_addCharacter(Console, "Test_delete Leader d10 3d10 3d10 3d10 3d10 2d8 2d8 Animal Brash Deadeye")
        Character creation of Test_delete the Leader has been successful!
        >>> Console.do_delete_character(Console, "Test_delete")
        Leader object has been removed.

        delete_character [Character Name]

        This command will delete the character
        """
        league = self.lm.get_current_league()
        character = league.find_character(args)
        league.remove_character(character)

    def do_replace_all_abilities(self,args):
        '''
        >>> Console.do_createLeague(Console,"Test")
        Test created
        >>> Console.do_addCharacter(Console, "Test_replace_all Leader d10 3d10 3d10 3d10 3d10 2d8 2d8 Animal Brash Deadeye")
        Character creation of Test_replace_all the Leader has been successful!
        >>> Console.do_replace_all_abilities(Console, "Test_replace_all Speedy Savvy Clever")
        New abilities added Speedy Savvy Clever

        replace_all_abilities [Character Name] [new ability1] [new ability 2] [new ability 3]

        Replaces all abilities on a character
        '''
        result = args.split(" ")
        league = self.lm.get_current_league()
        character = league.find_character(result[0])
        if len(result) == 0:
            print("You have not set any abilities")
        if len(result) == 2:
            character.set_abilities(arg1 = result[1])
            print("New abilities added " + result[1])
        if len(result) == 3:
            character.set_abilities(arg1 = result[1], arg2 = result[2])
            print("New abilities added " + result[1] + " " + result[2])
        if len(result) == 4:
            character.set_abilities(arg1 = result[1], arg2 = result[2], arg3 = result[3])
            print("New abilities added " + result[1] + " " + result[2] + " "
                  + result[3])

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
        import doctest
        doctest.testmod(verbose=True)
        console = Console()
        console.cmdloop()