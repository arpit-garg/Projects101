from urllib2 import urlopen
from json import load

def currency():
	
	val1 = raw_input("Enter the currency you want to convert from(e.g. USD,INR etc): ").upper()
	val2 = raw_input("Enter the currency you want to convert to(e.g. INR,USD etc): ").upper()
	val = input("Enter the amount you want to convert: ")

	#Using rate-exchange API http://rate-exchange.appspot.com
	url = 'http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=%d' %(val1, val2, val)

	response = urlopen(url)
	json_obj =  load(response)['v']

	print json_obj

def temp():
	
	source_unit = raw_input("Enter the temperature you want to convert from(f/c): ").upper()
	source_val = input("Enter the temp you want to convert: ")
	
	if source_unit == 'F':				#Converting from F -> C
		
		val = (source_val - 32) * (5/9)
		print "The temperature in Celsius is: %.2f" %val
	
	else:								#Converting from C -> F
		
		val = (source_val * 9/5) + 32
		print "The temperature in Fahrenheit is: %.2f" %val
		
def main():
	ch = 'y'
	while ch == 'y':
		print """
		Unit Converter
		1.Currency
		2.Temperature
		"""
			
		choice = input("What do you want to convert?\n>")
		
		if choice == 1:
			currency()
			
		elif choice == 2:
			temp()
		
		ch = raw_input("Do you want to perform more conversions(y/n): ")
		
if __name__ == '__main__':
	main()