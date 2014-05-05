""" Enter a number and have the 
program generate the Fibonacci 
sequence to that number 
or to the Nth number."""

n = int(raw_input("Enter number till you want to generate the sequence.\n> "))

fibo = [0 , 1]
i = 2
while i < n:

	fibo.append(fibo[i-1] + fibo[i-2])
	i+=1
	
print fibo