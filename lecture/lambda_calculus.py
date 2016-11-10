"""
lambda calculus
"""

# 1. turing machine
# 2. functional programming

# encoding values with functions

## True and false 
t = lambda a: lambda b: a
f = lambda a: lambda b: b

def py_pred(p):
	return p(True)(False)