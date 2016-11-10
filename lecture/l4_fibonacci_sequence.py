"""
lecture 4

Fibonacci sequence
each element is the sum of previous two elements

iteration
"""

# version 1
# use while
def fib(n):
	"""
	compute the n-th Fibonacci number 
	"""
	pred, curr = 0, 1
	k = 1
	while k < n:
		pred, curr = curr, pred+curr
		#print(str(curr))
		k+=1
	return curr


