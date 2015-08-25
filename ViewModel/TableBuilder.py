from ViewModel.RowBuilder import *


class TableBuilder(object):
    """Class design to take an input 2D STring array and format into a table"""

    def __init__(self):
        self.row_builder = RowBuilder(self)
        self.cell_widths = []

    def build_table(self, input_2d_array):
        # print("tablebuilder input:")
        # print(input_2d_array)
        output = ""
        input_2d_array = self.pad_table(input_2d_array)
        self.calc_largest_cells(input_2d_array)
        count = 0
        '''
        for entry in input_2d_array[0]:
            self.cell_widths.append(len(entry) + 2)
            count += 1
        '''
        for entry in input_2d_array:
            output += self.row_builder.build_row(entry, '|') + '\n'

        # remove the last endline char
        output = output[:(len(output) - 1)]

        table_with = 0
        for num in self.cell_widths:
            table_with += num + 1

        horizontal_border = '-' * (table_with + 1)
        output = horizontal_border + '\n' + output + '\n'
        output += horizontal_border

        self.cell_widths = []
        return output

    def get_cell_width(self, column_number):
        return self.cell_widths[column_number]

    def set_cell_width(self, column_number, width):
        self.cell_widths[column_number] = width

    def pad_table(self, input_2D_array):
        longest_row = 0
        for a in input_2D_array:
            if len(a) > longest_row:
                longest_row = len(a)

        for a in input_2D_array:
            while len(a) < longest_row:
                a.append("")

        return input_2D_array

    def calc_largest_cells(self, input_2D_array):
        # for i in range(len(input_2D_array[0])):
        #    self.set_cell_width(i,0)
        for entry in input_2D_array[0]:
            self.cell_widths.append(2)

        for a in input_2D_array:
            for i in range(len(a)):
                if len(a[i]) > self.get_cell_width(i):
                    # self.cell_widths[i] = len(a[i])
                    self.set_cell_width(i, len(a[i]) + 2)
