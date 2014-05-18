"""Next Prime Number - Have the program 
find prime numbers until the user chooses 
to stop asking for the next one."""

import re

def next_prime(current):
	
	next_prime = current + 1
	
	for i in range(2, next_prime):
		
		if next_prime % i == 0:
			next_prime += 1
		return next_prime
			


def main():
	
	current_prime = 2

	print "current_prime = 2 "

	while True:
		
		response = raw_input("Do you want the next prime number?(y/n)")
		
		
		if re.match(response,'y', flags = 1):
			current_prime = next_prime(current_prime)
			print current_prime
		else:
			break

if __name__ == '__main__':
	main()