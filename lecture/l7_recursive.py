"""
lecture 7

recursive functions
if the body of that function call it self directly or indirectly.

"""

# how to write recursive
# 1. verify the base cases
# 2. treat fact() as a functional abstraction
# 3. assume fact(n-1) is correct
# 4. verify that fact(n) is correct if fact(n-1) is correct


# sum the digits of a number
# 2013 -> 2+0+1+3 -> return 6
# without a while statement

def split(n):
	"""
	split n into (1) all but last digit (2) last digit
	"""
	return n // 10, n % 10
	
def sum_digitis(n):
	"""
	sum the digits of a number
	"""
	if n < 10: # check the base cases
		return n  # end condition: end here
	else: 
		all_but_last, last = split(n)
		return sum_digitis(all_but_last) + last # simpler problem
		
# !!! mutual recursive: two functions call each other !!!	
# Luhn algorithm
# right most digit -> the check digit
# moving left -> double every second digit
# if the doubling operation is greater than 9, sum the digit (eg. 7*2=14->1+4=5)
# take the sum of all the digits
# 1 3 8 7 4 3
# 2 3 7 7 8 3 = 30
# the Luhn sum of a valid credit card number is a multiple of 10

def luhn_sum(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
	all_but_last, last = split(n)
	luhn_digit = sum_digitis(2*last)
	if n < 10:
		return luhn_digit
	else:
		return luhn_sum(all_but_last) + luhn_digit
		
		
# iteration VS recursion
def sum_digitis_iter(n):
	digit_sum = 0
	while n > 0:
		n, last = split(n)
		digit_sum = digit_sum + last
	return digit_sum
	
def sum_digitis_rec(n, digit_sum):
	if n == 0:
		return digit_sum
	else:
		n, last = split(n)
		return sum_digitis_rec(n, digit_sum)
		



