from ViewModel.TableBuilder import *
# from ViewModel.RowBuilder import *
# from ViewModel.CellBuilder import *


class ViewModel(object):

    def build_table(self, input_2d_array):
        tbl = TableBuilder()
        return tbl.build_table(input_2d_array)

    def build_character_table(self, input_3D_array):
        tbl = TableBuilder()
        result = ""
        for table in input_3D_array:
            result += tbl.build_table(table)
            result += "\n"
        return result

        # stuff
    def display(self, input):
        print(input)
