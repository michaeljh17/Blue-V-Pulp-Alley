from ViewModel.TableBuilder import *
# from ViewModel.RowBuilder import *
# from ViewModel.CellBuilder import *
from ViewModel.Word_Art import *


class ViewModel(object):

    def build_table(self, input_2d_array):
        tbl = TableBuilder()
        return tbl.build_table(input_2d_array)

    def build_character_table(self, input_2D_array):
        # print(str(input_2D_array))
        tbl = TableBuilder()
        word_art = Word_Art()
        result = ""
        temp_array = []
        # Change name to word art heading and display it
        result = word_art.heading(str(input_2D_array[0]))
        # Display Table for type
        temp_array.append([word_art.sub_heading(input_2D_array[1][0]),
                           input_2D_array[1][1]])
        result += tbl.build_table(temp_array)

        # Display subheading - Skills with no Table
        result += "\n"
        result += word_art.sub_heading(input_2D_array[2][0])
        result += "\n"
        # Display table for skills
        headings = []
        for heading in input_2D_array[3]:
            headings.append(word_art.sub_heading(heading))
        temp_array = [headings, input_2D_array[4]]
        result += tbl.build_table(temp_array)
        # Dsiplay subheading - Abilities with no Table
        result += "\n"
        result += word_art.sub_heading(input_2D_array[5][0])
        result += "\n"
        # Dsiplay table for abilities
        temp_array = []
        headings = []
        for heading in input_2D_array[6]:
            headings.append(word_art.sub_heading(heading))
        temp_array.append(headings)
        temp_array.append(input_2D_array[7])
        try:
            temp_array.append(input_2D_array[8])
        except IndexError:
            None
        try:
            temp_array.append(input_2D_array[9])
        except IndexError:
            None
        result += tbl.build_table(temp_array)
        return result

    def create_heading(self, text):
        text = str(text)
        word_art = Word_Art()
        result = word_art.heading(text)
        self.display(result)

    def display(self, input):
        print(input)
