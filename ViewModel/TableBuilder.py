from RowBuilder import *

class TableBuilder(object):
    """Class design to take an input 2D STring array and format into a table"""

    def __init__(self):
        self.row_builder = RowBuilder(self)
        self.cell_widths = []
        
    def build_table(self, input_2d_array):
        print("start build table")
        print(input_2d_array)
        print(input_2d_array[0])
        output = ""
        print("start loop")

        count = 0
        for entry in input_2d_array[0]:            
            print(entry)            
            print(len(entry))
            print(count)
            print(self.cell_widths)
            self.cell_widths.append(len(entry) + 2)
            count += 1

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

        print(self.cell_widths)
        print("the output is")
        self.cell_widths = []
        return output

    def get_cell_width(self, column_number):
        return self.cell_widths[column_number]

    def set_cell_width(self, column_number, width):
        self.cell_widths[column_number] = width

