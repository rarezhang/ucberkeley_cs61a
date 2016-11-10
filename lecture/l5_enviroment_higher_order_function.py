"""
lecture 5
environment of higher order function
"""

def apply_twice(f, x):
	"""
	take another function as the argument
	"""
	return f(f(x))
	
def square(x):
	return x * x
	
print(apply_twice(square, 3))

###########################################

def repeat(f, x):
	while f(x) != x:
		x = f(x)
	return x
	
def g(y):
	return (y+5)//3  # '//'will git rid of the reminder
	
	
result = repeat(g, 6)
print(result)

###########################################

def make_adder(n):
	def adder(k):
		return k + n
	return adder