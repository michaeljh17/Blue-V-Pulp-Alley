from TableBuilder import *
from RowBuilder import *
from CellBuilder import *

test_data = [["Stallone","American","Short","Angry"],["Willis","Mexican","Bald","Epic"],["T-800","?","Tank","Liquid"]]
print(test_data[0])
tbl = TableBuilder()

print(tbl.build_table(test_data))