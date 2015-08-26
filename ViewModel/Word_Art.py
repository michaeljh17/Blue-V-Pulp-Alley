
class Word_Art(object):

    def convert_letter(self, letter):
        # when given a letter this method returns an array of four arrays
        # containing characters to draw the letter over four lines
        letter = letter.lower()
        return {
            'a': ["       ",
                  "  __ _ ",
                  " / _` |",
                  "| (_| |",
                  " \__,_|",
                  "       "],
            'b': [" _     ",
                  "| |__  ",
                  "| '_ \ ",
                  "| |_) |",
                  "|_.__/ ",
                  "       "],
            'c': ["      ",
                  "  ___ ",
                  " / __|",
                  "| (__ ",
                  " \___|",
                  "      "],
            'd': ["     _ ",
                  "  __| |",
                  " / _` |",
                  "| (_| |",
                  " \__,_|",
                  "       "],
            'e': ["      ",
                  "  ___ ",
                  " / _ \\",
                  "|  __/",
                  " \___|",
                  "      "],
            'f': ["  __ ",
                  " / _|",
                  "| |_ ",
                  "|  _|",
                  "|_|  ",
                  "     "],
            'g': ["       ",
                  "  __ _ ",
                  " / _` |",
                  "| (_| |",
                  " \__, |",
                  " |___/ "],
            'h': [" _     ",
                  "| |__  ",
                  "| '_ \ ",
                  "| | | |",
                  "|_| |_|",
                  "       "],
            'i': [" _ ",
                  "(_)",
                  "| |",
                  "| |",
                  "|_|",
                  "   "],
            'j': ["   _ ",
                  "  (_)",
                  "  | |",
                  "  | |",
                  " _/ |",
                  "|__/ "],
            'k': [" _    ",
                  "| | __",
                  "| |/ /",
                  "|   < ",
                  "|_|\_\\",
                  "      "],
            'l': [" _ ",
                  "| |",
                  "| |",
                  "| |",
                  "|_|",
                  "   "],
            'm': ["           ",
                  " _ __ ___  ",
                  "| '_ ` _ \ ",
                  "| | | | | |",
                  "|_| |_| |_|",
                  "           "],
            'n': ["       ",
                  " _ __  ",
                  "| '_ \ ",
                  "| | | |",
                  "|_| |_|",
                  "       "],
            'o': ["       ",
                  "  ___  ",
                  " / _ \ ",
                  "| (_) |",
                  " \___/ ",
                  "       "],
            'p': ["       ",
                  " _ __  ",
                  "| '_ \ ",
                  "| |_) |",
                  "| .__/ ",
                  "|_|    "],
            'q': ["       ",
                  "  __ _ ",
                  " / _` |",
                  "| (_| |",
                  " \__, |",
                  "    |_|"],
            'r': ["      ",
                  " _ __ ",
                  "| '__|",
                  "| |   ",
                  "|_|   ",
                  "      "],
            's': ["     ",
                  " ___ ",
                  "/ __|",
                  "\__ \\",
                  "|___/",
                  "     "],
            't': [" _   ",
                  "| |_ ",
                  "| __|",
                  "| |_ ",
                  " \__|",
                  "     "],
            'u': ["       ",
                  " _   _ ",
                  "| | | |",
                  "| |_| |",
                  " \__,_|",
                  "       "],
            'v': ["       ",
                  "__   __",
                  "\ \ / /",
                  " \ V / ",
                  "  \_/  ",
                  "       "],
            'w': ["          ",
                  "__      __",
                  "\ \ /\ / /",
                  " \ V  V / ",
                  "  \_/\_/  ",
                  "          "],
            'x': ["      ",
                  "__  __",
                  "\ \/ /",
                  " >  < ",
                  "/_/\_\\",
                  "      "],
            'y': ["       ",
                  " _   _ ",
                  "| | | |",
                  "| |_| |",
                  " \__, |",
                  " |___/ "],
            'z': ["     ",
                  " ____",
                  "|_  /",
                  " / / ",
                  "/___|",
                  "     "],
            ' ': ["   ", "   ", "   ", "   ", "   ", "   "],
        }.get(letter, ["", "", "", "", "", ""],)

    def combine_arrays(self, *args):
        # when given 2 or more arrays this method returns an array that has
        # combined each of the elements
        # combine_arrays(["Array1String1", "Array1String2"],
        # ["Array2String1", "Array2String2"])
        # becomes
        # ["Array1String1Array1String2", "Array2String1Array2String2"]

        # find the array with the largest set of elements and ensure result
        # has enough elements to handle it
        result = []
        largest_array_length = 0
        for the_array in args:
            if len(the_array) > largest_array_length:
                largest_array_length = len(the_array)

        for i in range(largest_array_length):
            result.append("")

        if len(args) < 2:
            print("combine_arrays() must be given at least two arrays")
            return

        for count, the_array in enumerate(args):
            for i, the_string in enumerate(the_array):
                result[i] += the_array[i]

        return result

    def change(self, theString):
        # when given a string this method converts each letter in it into
        # arrays and then joins the arrays to display the word as text art
        result = []
        #
        for letter in theString:
            result.append(self.convert_letter(letter))

        result = self.combine_arrays(*result)
        return_string = ""

        for string in result:
            return_string += string + "\n"

        return return_string
