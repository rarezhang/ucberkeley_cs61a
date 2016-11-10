"""
lecture 4

- generalization of number
- generalization of function: higher order function
	- take a function as an argument
	- return a function

"""
# generalization of number
# version 1
def area_square(r):
	assert r > 0, 'a length must be positive'
	return r * r
	
def area_circle(r):
	from math import pi
	return r * r * pi

def area_hexagon(r):
	return r * r * sqrt(3) / 2
	
# version 2
def area(r, shape_constant):
	assert r > 0, 'a length must be > 0'
	return r * r * shape_constant
	
# generalization of function
# version 1
def sum_naturals(n):
	"""
	>>> sum_naturals(5)
	15
	"""
	total, k = 0, 1
	while k <= n:
		total, k =total + k, k + 1
	return total
	
def sum_cubes(n):
	"""
	>>> sum_cubes(5)
	225
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total+pow(k,3), k+1
	return total
	
# version 2
def identity(k):
	return k 
	
def cube(k):
	return pow(k, 3)

def pi_term(k):
	from operator import mul
	# mul(a,b): return a*b
	return 8 / mul(4*k-3, 4*k-1)
	
def summation(n, term):
	"""
	term is a function !!!
	>>> summation(5, cube)
	225	
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total+term(k), k+1
	return total
	
############################
# return function
def make_adder(n):
	"""
	return a function that takes one arguemnt K return K+n
	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder # adder is a function adder(k), adder already know the value of n--> by make_adder(n)
	


