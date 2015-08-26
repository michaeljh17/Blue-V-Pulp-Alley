from ViewModel.TableBuilder import *
# from ViewModel.RowBuilder import *
# from ViewModel.CellBuilder import *
from ViewModel.Word_Art import *


class ViewModel(object):

    def build_table(self, input_2d_array):
        tbl = TableBuilder()
        return tbl.build_table(input_2d_array)

    def build_character_table(self, input_3D_array):
        tbl = TableBuilder()
        word_art = Word_Art()
        result = ""
        for count, table in enumerate(input_3D_array):
            if count == 0:
                table[0][1] = word_art.change(table[0][1])
            result += tbl.build_table(table)
            result += "\n"
        return result

        # stuff
    def display(self, input):
        print(input)
