"""
lecture 24
exceptions
"""

# built-in mechanism in a programming language to declare and respond to exceptional conditions 

# python raises an exception whenever an error occurs

# exceptions can be handled by the program, preventing the interpreter from halting

# un-handled exceptions will cause python to halt execution and print a stack trace 

## exception
# objects
# have classes with constructors
# enable non-local continuations of control
# e.g., if f() calls g()
# g() calls h()
# exception can shift control from h() to f() without waiting for g to return

## assert statements
'''
assert <expression>, <string>
python3 -O to avoid all assert statement
'''
assert False, 'Error'



## raise statement
'''
raise <expression>

TypeError: a function was passed the wrong number / type of argument
NameError: a name wasn't found
KeyError: a key wasn't found in a dictionary
RuntimeError: catch all for troubles during interpretation
'''
raise TypeError('Bad argument')


## try statement
# prevent a program from terminating
'''
try:
	<try suite>
except <exception class> as <name>
	<except suite>
'''
try:
	x = 1/0
except ZeroDivisionError as e:
	print('handling a', type(e))
	x = 0
	

def invert(x):
	y = 1/x
	print("Never printed if x is 0")
	return y
	
def invert_safe(x):
	try:
		return invert(x)
	except: ZeroDivisionError as e:
		print('handled', e)
		return 0
	




