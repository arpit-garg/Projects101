"""Prime Factorization - Have the user 
enter a number and find all Prime Factors 
(if there are any) and display them.
"""
def prime(n):					#Check for prime numbers.
	for i in range(2, n):
		if(n % i == 0):
			return False
		else:
			return True
	
x = int(raw_input("Enter a number you want prime factors of \n>"))

prime_factors = []

if (x % 2 == 0):
	prime_factors.append(2)
	

for i in range(2, x + 1):
	if(x % i == 0):
		if(prime(i)):
			prime_factors.append(i)
		x /= i;

print prime_factors
