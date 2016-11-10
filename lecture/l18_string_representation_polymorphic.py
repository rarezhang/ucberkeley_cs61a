"""
lecture 18
string representation

"""

# repr()
# returns a python expression that evaluates to an equal object
# eval(repr(object)) == object

12e12  # 12000000000000.0
print(12e12)
print(repr(12e12)) # 12000000000000.0

print(repr(min))  # <built-in function min>

# str()
import datetime
today = datetime.date(2014, 10, 13)
print(repr(today))  # datetime.date(2014, 10, 13)

print(today)  # 2014-10-13
print(str(today))  # 2014-10-13


# polymorphic functions
# a function that applies to may different form of data

class Bear:
	def __init__(self):
		self.__repr__ = lambda: 'oski'
		self.__str__ = lambda: 'this bear instance'
	def __repr__(self):
		return 'Bear(h)'
	def __str__(self):
		return 'this is a bear'
		
Bear()  # Bear(h)
oski = Bear()
oski.__repr__()  # 'Bear(h)'

def print_bear():
	oski = Bear()
	print(oski)  # this is a bear
	print(str(oski)) # this is a bear
	print(repr(oski)) # Bear(h)
	print(oski.__repr__()) # oski
	print(oski.__str__()) # this bear instance
	
print_bear()

def repr(x):
	return type(x).__repr__(x)
	
def str(x):
	t = type(x)
	if hasattr(t, '__str__'):
		return t.__str__(x)
	else:
		return repr(x)

# property methods
# @property decorator on a method designates that it will be called whenever it is looked up on an instance 
class Rational:
	def __init__(self, numer, denom):
		self.numer = numer
		self.denom = denom
		
	def __repr__(self):
		return 'Rational({0}, {1})'.format(self.numer, self.denom)
		
	def __str__(self):
		return '{0}/{1}'.format(self.numer, self.denom)
	
	@property	
	def float_value(self):
		return self.numer / self.denom

Rational(1,2)  # Rational(1,2)	
str(Rational(1,2)) # 1/2
# before add @property
Rational(1,2).float_value # <bound method Rational.float_value of Rational(1, 2)>
#Rational(1,2).float_value() # 0.5
# after add @property
x = Rational(1,2)
x.float_value  # 0.5
# just change the numer
x.numer = 5
x.float_value  # 2.5


# multiple representations of abstract data
# example: complex numbers
