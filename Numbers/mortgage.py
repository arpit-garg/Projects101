"""
Mortgage Calculator - 
Calculate the monthly payments 
of a fixed term mortgage over given 
Nth terms at a given interest rate. 
Also figure out how long it will take 
the user to pay back the loan.
"""
import math

p = input("Enter the principal amount\n>")
i = input("Enter the annual rate of interest\n>")
t = input("Enter the loan term\n>")

i = i / 12
n = t * 12

x = math.pow(1 + i, n)

m = p * ( i * x) / (x -1)

print "The Mortgage payment is: %.2f" % m
