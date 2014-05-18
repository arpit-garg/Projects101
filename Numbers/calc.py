"""
Calculator - A simple calculator to do basic operators
"""

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

op = raw_input("Enter the operation ('+', '-', '*', '/') ")			#Check for operator

if op not in '+-*/':
	print "Invalid Operator"
else:
	print "%d %s %d = %.2f" %(num1, op, num2, eval(str(num1) + op + str(num2))	#Using eval() to evaluate string.