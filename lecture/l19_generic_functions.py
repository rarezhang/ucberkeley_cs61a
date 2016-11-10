"""
generic functions

apply to multiple arguments that don't share a common interface:
-arithmetic system over related types 
-operator overloading
-type dispatching
-type coercion
"""

from fractions import gcd
from math import atan2, sin, cos, pi


## special method names 
'''
__init__: invoked automatically when an object is constructed
__repr__: invoked to desplay an obect as a string
__add__: invoked to add one object to another
__bool__: invoked to convert an object to True or False
'''

'''
zero, one, two = 0, 1, 2
one.__add__(two) 
zero.__bool__()
'''

'''
class Number:
	"""
	a number
	why: use number as base class so we can use '+'
	and can still use the add and mul functions in Rational and Complex class
	"""
	def __add__(self, other):
		return self.add(other)
		
	def __mul__(self, other):
		return self.mul(other)
'''
## cross-type arithmetic 
# type dispatching: 
# define a different function for each possible combination of types for which an operation is valid (e.g., addition)
def add_complex_and_rational(c, r):
	return ComplexRI(c.real + r.numer/r.denom, c.imag)

def add_rational_and_complex(r, c):
	return add_complex_and_rational(c, r)


class Number:
	"""
	"""
	def __add__(self, other):
		if self.type_tag == other.type_tag:
			return self.add(other)
		elif (self.type_tag, other.type_tag) in self.adders: # check the combination of type_tags
			return self.cross_apply(other, self.adders)
	
	def cross_apply(self, other, cross_fns):
		cross_fn = cross_fns[(self.type_tag, other.type_tag)]
		return cross_fn(self,other)

		
	adders = {('com', 'rat'): add_complex_and_rational,
	('rat', 'com'): add_rational_and_complex}
		
	def __mul__(self, other):
		return self.mul(other)


## Rational numbers
class Rational(Number):
	"""
	a rational number represented as a numerator and denominator
	"""
	type_tag = 'rat'
	def __init__(self, numer, denom):
		g = gcd(numer, denom)  # greatest common divisor
		self.numer = numer // g
		self.denom = denom // g
		
	def __repr__(self):
		return 'Rational({0},{1})'.format(self.numer, self.denom)
	
	def add(self, other):
		nx, dx = self.numer, self.denom
		ny, dy = other.numer, other.denom
		return Rational(nx * dy + ny * dx, dx * dy)
		
	def mul(self, other):
		numer = self.numer * other.numer
		denom = self.denom * other.denom
		return Rational(numer, denom)
		
'''		
third = Rational(1,3)
sixth = Rational(1,6)
third.add(sixth)  # Rational(1,2)
third.mul(sixth)  # Rational(1,18)
'''

## Complex numbers
class Complex(Number):
	type_tag = 'com'
	def add(self, other):
		return ComplexRI(self.real + other.real, self.imag + other.imag)
		
	def mul(self, other):
		return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)
		
class ComplexRI(Complex):
	"""
	a rectangular representation
	"""
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
		
	@property
	def magnitude(self):
		return (self.real**2 + self.imag**2)**0.5
		
	@property
	def angle(self):
		return atan2(self.imag, self.real)
		
class ComplexMA(Complex):
	"""
	a polar representation
	"""
	def __init__(self, magnitude, angle):
		self.magnitude = magnitude
		self.angle = angle
	
	@property
	def real(self):
		return self.magnitude * cos(self.angle)
		
	@property
	def imag(self):
		return self.magnitude * sin(self.angle)

'''		
i = ComplexRI(0,1)
i.mul(i)
'''	

'''
# use + and *
Rational(1,3) + Rational(1, 6)	# Rational(1,2)

i = ComplexMA(1, pi/2)
i*i
'''

'''
r = Rational(1,2)
c = ComplexRI(1,1)
r+c
'''
	
