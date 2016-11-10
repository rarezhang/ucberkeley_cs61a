"""
lecture 10
Data Abstraction 
"""

# data
print(type(1))
## <class 'int'>  --> represents int exactly
print(type(2.2))
## <class 'float'> --> represents real numbers approximately eg. 0.2222222222222222 == 0.2222222222222227 True
print(type(1+1j))
## <class 'complex'>
print(type(True))
## <class 'bool'>
print(1+1.2)
## <class 'float'>

# object
# represent information
# (1) data (2) behavior --> abstraction
# object-oriented programming

from datetime import date
today = date(2016, 2, 29)
freedom = date(2016, 5, 20)
print(str(freedom - today))
print(today.year)
print(today.day)
print(today.strftime("%A %B %d"))  # a method for the object 'today' string format of time
print(type(today))  
## <class 'datetime.date'>


# data abstraction 
# compound objects combine objects together
## parts -> how data are represented
## units -> how data are manipulated
# data abstraction: enforce an abstraction barrier between (1) representation (2) use

# pair representation
## normal way
def pair_1(x, y):
	return [x, y]

def select_1(p, i):
	return p[i]
	
## functional pair representation
def pair_2(x, y):
	def get(index):
		if index == 0:
			return x
		elif index == 1:
			return y
	return get

def select_2(p, i):
	return p(i)