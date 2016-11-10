"""
lecture 9 
function example 
"""

# functional abstraction
## argument
## function

# function name 
## meaning or purpose
## effect, behaviour, value returned

# test-driven development
## test: domain, range, behavior of a function
## tricky edge cases
## develop incrementally and test each piece before moving
## experiment with function 

def gcd(m, n):
	"""
	returns the largest k that divides both m, n
	eculidean algorithm
	>>> gcd(12, 8)
	4
	>>> gcd(16, 2)
	2
	>>> gcd(16, 8)
	8
	>>> gcd(2, 16)
	2
	>>> gcd(5, 5)
	5
	"""
	if n % m == 0:
		return m
	elif m < n:
		return gcd(n,m)
	else: # m > n
		return gcd(m-n, n)
		
		
# function decorators
# a feature of python
def trace1(fn):
	"""
	returns a version of fn that first print it is called 
	fn param: a function of 1 argument
	"""
	def traced(x):
		print('calling', fn, 'on argument', x)
	return traced

def square(x):
	return x * x

	
# decorators -> high order function -> # sum_squares_up_to = trace1(sum_squares_up_to)
@trace1
def sum_squares_up_to(n):
	"""
	>>> sum_squares_up_to(1)
	1
	>>> sum_squares_up_to(0)
	0
	>>> sum_squares_up_to(2)
	5
	"""
	if n < 2:
		return n
	else:
		return square(n) + sum_squares_up_to(n-1)
		
#############################
# what would python print
print(5) # return None, print 5
print(print(5))  # print None
# 5
# None


def delay(arg):
	"""
	a function that takes any argument
	returns a function that returns that argument
	"""
	print('delayed')
	def g():
		return arg # names in nested def statements can refer to their enclosing scope
	return g
	
delay(delay)()(6)()
#4 delay(delay)()(6)  () --> apply the first part to the second part
#3 delay(delay)()    (6) --> g(6) <g=delay()> print 'delayed' return 6
#2 delay(delay)      ()  --> call g 
#1 delay(delay) -->   print 'delayed'  return g=delay()

'''
# interactive output
delayed
delayed
6
'''

print(delay(print)()(4))
#4 print()		--> print None; return None (since last return is None: this None won't show on screen)
#3 print()		delay(print)()(4)  -->print(4) print '4' 	return None 
#2 delay(print)()	--> call g()=print()()
#1 delay(print)		--> print 'delayed' return g=print()

'''
# interactive output
delayed
4
None
'''

from operator import add, mul
def square(x): 
	return mul(x,x)
	
def pirate(arggg):
	print('matey')
	def plunder(arggg):
		return arggg
	return plunder
	
add(pirate(3)(square)(4), 1)
#4 add([], 1)		--> add(16, 1)  return 17
#3 pirate(3)(square)		(4)		--> call square()(4)=square(4)	return 16
#2 pirate(3)				(square)	--> call plunder()=plunder(square)  return square()
#1 pirate(3)		--> print 'matey' return plunder()

'''
# interactive output
matey
17
'''

#pirate(pirate(pirate))(5)(7)
 
#1 pirate(pirate)	--> print 'matey'; return plunder
#2 pirate(pirate(pirate))  --> print 'matey'; return plunder()
#3 pirate(pirate(pirate))(5)  --> call plunder()(5)= plunder(5)	  return 5
#4 pirate(pirate(pirate))(5)(7)  --> 5(7) TypeError: int object is not callable

'''
# interactive output
matey
matey
TypeError: int object is not callable
'''

def horse(mask):
	horse = mask
	def mask(horse):
		return horse
	return horse(mask)

mask = lambda horse: horse(2)

horse(mask)
# global
## horse = def horse(mask): ...
## mask = lambda horse: horse(2)
# call horse(mask)
# f1: parent=global
## horse = lambda horse: horse(2)
## mask = def mask(horse): return horse
'''
def horse(mask):
	horse = mask # mask = lambda horse: horse(2)
	def mask(horse):
		return horse
	return horse(mask)  # call horse(mask)
'''
# call horse(mask)
# lecture 9 - video 5
# return 2

 