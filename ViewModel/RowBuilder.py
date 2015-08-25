from ViewModel.CellBuilder import *


class RowBuilder(object):
    """description of class"""

    def __init__(self, table_builder):
        self.cell_builder = CellBuilder()
        self.my_table_builder = table_builder

    def build_row(self, input_array, border_character):
        output = "|"
        count = 0
        for entry in input_array:
            cell_width = self.my_table_builder.get_cell_width(count)
            output += self.cell_builder.build_cell(entry, cell_width,
                                                   border_character)
            count += 1
        return output
