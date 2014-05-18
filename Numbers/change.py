"""
Change Return Program - 
The user enters a cost and 
then the amount of money given. 
The program will figure out the 
change and the number of quarters, 
dimes, nickels, pennies needed for the change.
"""


cost = input("Enter the total cost:\n>")		#Total billing	
amount = input("Enter the amount given:\n>")	#Amount given by customer

dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0	

if cost ==  amount:								#Check if exact amount given
	print "The amount looks perfect."
	
elif amount < cost:
	print "You gotta take more money."

else:
	change = amount - cost
	print "The change left is %.2f" % change	#Total change
	
	if change >= 1:								#Change in dollars
		dollars = int(change)
		change -= dollars
	
	if change >= 0.25:							#Change in quarters
		quarters = int(change / 0.25)
		change -= quarters*0.25
	
	if change >= 0.10:							#Change in dimes
		dimes = int(change / 0.10)
		change -= dimes*0.10
	
	if change >= 0.05:							#Change in nickels
		nickels = int(change / 0.05)
		change -= nickels*0.05
	
	if change >= 0.01:							#Change in pennies
		pennies = change*0.01
		
print "The change is \n%d dollars\n%d quarters\n%d dimes\n%d nickels and\n%d pennies" \
		% (dollars, quarters, dimes, nickels, pennies)