"""
Find Cost of Tile to Cover W x H Floor - 
Calculate the total cost of tile it would 
take to cover a floor plan of width and height, 
using a cost entered by the user.
"""

cost = input("Enter the cost per sq feet:\n> ")
width = input("Enter the width of floor:\n> ")
height = input("Enter the height of floor:\n> ")

print "The cost of %.2f sq feet floor is %.2f" % (width * height, width * height * cost)