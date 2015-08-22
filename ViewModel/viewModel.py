from ViewModel.TableBuilder import *
#from ViewModel.RowBuilder import *
#from ViewModel.CellBuilder import *

class ViewModel(object):

    def build_table(self,input_2d_array):
        tbl = TableBuilder()
        return tbl.build_table(input_2d_array)

    def display(self, input):
        print(input)