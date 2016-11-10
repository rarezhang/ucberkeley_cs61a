"""
lecture 6

newtons_method

high order functions:
takes one or more functions as arguments,
returns a function as its result.
"""

# lambda expression
#square = lambda x,y: x*x*y

# currying 
def make_adder(n):
	"""
	return a function f=lambda k: n+k
	n: is the para of function make_adder
	k: is the para for the returned function f
	>>> make_adder(2)(3)
	5
	"""
	return lambda k: n+k

add = lambda x,y: x+y  # add(2,3)

''''	
def curry2(f):
	"""
	curry2: means take 2 parameters
	get a function 
	"""
	def g(x):
		def h(y):
			return f(x,y) #h(x): return f(x,y)
		return h #g(x) return h: is a function of f(x,y)
	return g #curry2(f) return g: is a function of f(x,y)
'''

curry2 = lambda f: lambda x: lambda y: x+y  # the lambda version of curry2

'''
m = curry2(add) 
print(m) # function curry2; g
add_three = m(3)
print(add_three) # function curry2; g(x) x=3; h
result = add_three(2) # function curry2; g(x) x=3; h(y) y=2
print(add_three) 
print(result)
'''

####################################
# version 1: special cases
'''
def square_root(a):
	"""
	!!!cannot handle eg.square(2)
	"""
	x = 1 # initial random guess
	while x * x != a:
		print (x)
		x = square_root_update(x,a)
	return x

	
def square_root_update(x, a):
	return (x + a/x) / 2

	
def cube_root(a):
	"""
	!!!cannot handle eg.cube(3)
	"""
	x = 1 # initial random guess
	while x * x * x != a:
		print (x)
		x = cube_root_update(x,a)
	return x


def cube_root_update(x, a):
	return (2*x + a/(x*x))/3
'''

# version 2: still special cases
# general improve function 
# handle unlimited issues
'''
def square_root_update(x, a):
	return (x + a/x) / 2
	
def cube_root_update(x, a):
	return (2*x + a/(x*x))/3
	
	
def improve(update, close, guess=1, max_update=20):
	"""
	keep trying sth till success
	(can handle unlimited decimals)
	"""
	k = 0 # count the update
	while not close(guess) and k < max_update:
		guess = update(guess)
		k+=1
	return guess

def approx_eq(x, y, tolerance=1e-15):
	"""
	compare if two numbers are close enough
	"""
	#print(x,y)
	return abs(x-y) < tolerance
	
def square_root(a):
	"""
	now can handle some unlimited digits
	
	"""
	def update(x):
		return square_root_update(x,a)
	def close(x):
		return approx_eq(x*x, a)	
	return improve(update, close) # 'improve' return a number, give the initial value of x=1
	
def cube_root(a):
	"""
	similar to square_root()
	but use lambda expression
	"""
	return improve(lambda x: cube_root_update(x, a), lambda x: approx_eq(x*x*x, a),a)
'''

# version 3: general method 
# get general root update functions
'''
def square_root(a):
	def f(x):
		return x*x - a
	def df(x):
		return 2*x
	return find_zero(f, df)
	
def cube_root(a):
	return find_zero(lambda x: x*x*x-a, lambda x: 3*x*x)

def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newtow_update(f, df), near_zero)

def newtow_update(f, df):
	def update(x):
		return x - f(x) / df(x)
	return update  # return a function, the x in f(x) will be the 'guess' in 'improve'
	
def improve(update, close, guess=1, max_update=20):
	"""
	keep trying sth till success
	(can handle unlimited decimals)
	"""
	k = 0 # count the update
	while not close(guess) and k < max_update:
		guess = update(guess)
		k+=1
	return guess

def approx_eq(x, y, tolerance=1e-15):
	"""
	compare if two numbers are close enough
	"""
	#print(x,y)
	return abs(x-y) < tolerance
'''
	
# version 4: more general method 
# get general f() and df()
def root(a, n):
	"""
	get a ^ (1/n)
	"""
	def f(x):
		return power(x, n) - a
	def df(x):
		return n * power(x, n-1)
	return find_zero(f, df)

def power(x, n):
	"""
	x ** n
	"""
	product, k = 1, 0
	while k < n:
		product, k = product * x, k+1
	return product
	
def find_zero(f, df):
	def near_zero(x):
		return approx_eq(f(x), 0)
	return improve(newtow_update(f, df), near_zero)

def newtow_update(f, df):
	def update(x):
		return x - f(x) / df(x)
	return update  # return a function, the x in f(x) will be the 'guess' in 'improve'
	
def improve(update, close, guess=1, max_update=20):
	"""
	keep trying sth till success
	(can handle unlimited decimals)
	"""
	k = 0 # count the update
	while not close(guess) and k < max_update:
		guess = update(guess)
		k+=1
	return guess

def approx_eq(x, y, tolerance=1e-15):
	"""
	compare if two numbers are close enough
	"""
	#print(x,y)
	return abs(x-y) < tolerance
