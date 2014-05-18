"""
Binary to Decimal and Back Converter - 
Develop a converter to convert a decimal 
number to binary or a binary number to 
its decimal equivalent.
"""

ch = input("What do you want to do\n1.Binary to Decimal\n2.Decimal to Binary\n>")

if ch == 1:
	
	bin = raw_input("Enter the Binary number:\n>")
	print int(bin, 2)					#Converting binary to decimal using int()
	
elif ch == 2:
	
	dec = input("Enter the decimal number:\n>")
		
	rem = []
	quot = dec
	binary = ""
	i = 0
	while quot > 0:						#Extracting the remainder in binary form
		rem.append( str (quot % 2))
		quot /= 2
		
	rem.reverse()						#Reversing the remainders to get actual binary form
	binary = "".join(rem)
	print binary
	
else:
	print "Invalid choice"