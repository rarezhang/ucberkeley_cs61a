"""
lecture 21 
time
space
"""

# implementations of the same functional abstraction can require different amounts of time

# e.g., how many factors does a positive integer n have

def factors(n):
	"""
	time: number of division 
	(1) slow: test each k from 1 through n --> n
	(2) fast: test each k from 1 to square root n
		for every k, n/k is also a factor --> n ** 0.5
	"""
	total = 0
	for k in range(1, n+1):
		if divides(k, n):
			total += 1
	return total

from math import sqrt
def factors_fast(n):
	total = 0
	sqrt_n = sqrt(n)
	k = 1
	while k < sqrt_n:
		if divides(k, n):
			total += 2 # one for k, one for n/k
		k += 1
	if k*k == n:
		total += 1  # perfect sqrt, add the sqrt value, n/sqrt=sqrt, so just need add 1
	return total
	
	
def divides(k, n):
	return n%k == 0
	
# the consumption of space

# order of growth

# exponentiation
def exp(b, n):
	if n == 0:
		return 1
	return b* exp(b, n-1)
	
def square(x):
	return x*x
def fast_exp(b, n):
	if n == 0:
		return 1
	elif n % 2==0:
		return square(fast_exp(b, n//2))
	else:
		return b * fast_exp(b, n-1)
	
