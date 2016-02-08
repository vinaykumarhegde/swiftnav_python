#! /usr/bin/env python
from sys import argv,exit
from math import sqrt, ceil


'''
Function: isPrime
Inputs: n: Value to be checked
Output: Boolean (True if prime, False otherwise)
Algorithm: Check if any integer from 2 ro sqrt(n) can divide
	the number. If yes, number is not a prime. If no, number
	is prime.
	Drawbacks: Polynomial time execution.
	Alterate Algorithms: 
		- Miller-Rabin test (Probabilistic)
		- AKS test (Deterministic)
'''
def isPrime(n):
	for i in range(2,int(ceil(sqrt(n)))):
		if(n%i == 0):
			return False
	print "BuzzFizz",
	return True


'''
Function: divby3
Input: n - Value to be checked
Output: prints Buzz and returns True if divisible by 3
		returns False instead
'''
def divby3(num):
	if(num%3 == 0):
		print "Buzz",
		return True
	return False


'''
Function: divby5
Input: n - Value to be checked
Output: prints Fizz and returns True if divisible by 5
		returns False instead
'''
def divby5(num):
	if(num%5 == 0):
		print "Fizz",
		return True
	return False


'''
Function: fib
Inputs: n (number of items in fibonacci series)
Output: Fibonacci series with
		- "Buzz" displayed when number is divisible by 3
		- "Fizz" displayed when number is divisible by 5
		- "BuzzFizz" displayed when number is a prime
		- value of F(n) otherwise.
'''
def fib(n,a=1,b=1):
	if(n==0):
		return
	num = a + b
	# if( divby3(num) or divby5(num) or isPrime(num)):
	if any( (divby3(num) , divby5(num) , isPrime(num))):
		pass
	else:
		print num,
	print ""
	fib(n-1,b,num)
	return



def main(n):
	if(n<1):
		print "Enter value 1 or more."
	elif(n==1):
		print "1"
	else:
		print "1\n1"
		fib(n-2)


if __name__ == '__main__':
	if(len(argv) != 2):
		print "Please enter ./fib.py <n>"
		exit(1)
	main(int(argv[1]))
	exit(0)