"""
graph paper

"""

import sys

boxrows = int(input("How many rows of boxes should we print? "))
boxcolumns = int(input("How many columns do you need? "))
spacerows = int(input("How many spaces per box do you require? "))
spacecolumns = int(input("How many spaces per column do you require? "))

for boxrow in range(boxrows):
    for boxcolumn in range(boxcolumns):
        print ("|", end ="")
        for spacerow in range(spacerows):
            print("-", end ="")
    print("|")
                   
    for spacerow in range(spacerows):
        for boxcolumn in range(boxcolumns):
            print("+", end ="")
            for spacerow in range(spacecolumns):
                print(" ", end ="")
        print("+")

for boxcolumn in range(boxcolumns):
    print("|", end ="")
    for spacerow in range(spacecolumns):
        print("-", end ="")
print("+")

sys.exit(0)
