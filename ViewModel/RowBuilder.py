from CellBuilder import *

class RowBuilder(object):
    """description of class"""

    def __init__(self, table_builder):
        self.cell_builder = CellBuilder()
        self.my_table_builder = table_builder

    def build_row(self, input_array, border_character):
        print(input_array)
        output = "|"
        count = 0
        for entry in input_array:
            output += self.cell_builder.build_cell(entry,self.my_table_builder.get_cell_width(count), border_character)
            count += 1
        return output


