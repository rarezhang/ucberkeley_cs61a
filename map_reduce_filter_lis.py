# python
# functional programming
# map, reduce, filter, list comprehension

items = [1,2,3,4,5]

# map
# apply an operation to each item
# map(aFunction, aSequence) -> return map object
# faster than a manually coded for loop!!!

def squ_f(x):
	return x*x
v1 = list(map(squ_f, items))

v2 = list(map(lambda x: x*x, items))

print(v1)
# [1, 4, 9, 16, 25]
print(v2)
# [1, 4, 9, 16, 25]


# lambda -> aFunction
# list of function -> aSequence
# each item in the list -> apply functions separately

square = lambda x: x**2
cube = lambda x: x**3

functions = [square, cube]  # a list of functions !!!

for r in items:
	# high order functions 
	# lambda x: x(r) -> x is function mapped from 'functions'
	# r -> the numeric value from 'items'
	v = map(lambda x: x(r), functions)
	print(type(v)) # class map
	print(list(v)) # v: map object

# items = [1,2,3,4,5]
# [1, 1]
# [4, 8]
# [9, 27]
# [16, 64]
# [25, 125]

#  sends items taken form sequences in parallel as distinct arguments to the function

# pow(a,b) = a**b
list_a = [2, 3, 4]
list_b = [10,11,12]

v = list(map(pow, list_a, list_b))
print(v)
# [2**10, 3**11, 4*12] -> [1024, 177147, 16777216]


l1 = [[1,1],[2,2]]
l2 = [[3,3],[4,4]]
v = list(map(zip,l1,l2))
for i in list(map(zip,l1,l2)):
	print(list(i))
# [(1, 3), (1, 3)]
# [(2, 4), (2, 4)]


# filter
# filter extracts each element in the sequence for which the function returns True
# filter(aFunction, aSequence)

def greater_than_2(x):
	return x > 2
v1 = filter(greater_than_2, items)

v2 = list(filter(lambda x: x>2, items))

# items = [1,2,3,4,5]
print(type(v1)) # class filter
print(list(v1)) # [3,4,5]
print(v2)



# reduce
# reduce a list to a single value by combining elements via a supplied function -> return a single results
# reduce(aFunction, aSequence)
from functools import reduce
def product_two(x,y):
	return x*y
v1 = reduce(product_two, items)

v2 = reduce(lambda x,y: x*y, items)	

print(type(v1)) # class int
print(v1) # 120 = 1*2*3*4*5
print(v2)



# list comprehension

# items = [1,2,3,4,5]
s = [x for x in items]
print(s)  # [1,2,3,4,5]
s = [x**2 for x in items]
print(s)  # [1, 4, 9, 16, 25]
s = [x for x in items if x > 2]
print(s)  # [3,4,5]

n = 38
def add_digits(num):
	if num < 9:
		return num
	else:
		return add_digits(reduce(lambda x,y: int(x) + int(y), str(num)))

print(add_digits(n))
