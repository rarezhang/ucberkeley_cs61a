"""
lecture 11
sequence
list
"""

digits = [1,8,2]
print(digits * 2)
# [1,8,2,1,8,2]

print(list(map(lambda x:2*x, digits)))
# [2,16,4]

print([2*x for x in digits])
# [2,16,4]

# for statement
def count(s, value):
	"""
	count the number of times that value occurs in sequence s
	>>> count([1,11,1,2,1], 1)
	3
	"""
	## version 1
	'''
	total, index = 0, 0
	while index < len(s):
		element = s[index]
		if element == value:
			total += 1
		index += 1
	return total
	'''
	## version 2
	total = 0
	for element in s:
		if element == value:
			total += 1
	return total

# function tools to do this work
items = [1,11,1,2,1]
i = 1
# 1
print(items.count(i))
# 2
print(len([x for x in items if x == i]))
# 3
print(len(list(filter(lambda x: x == 1, items))))


# sequence unpacking in for statements
pairs = [[1,2],[2,2]]
same_count = 0
for x, y in pairs:
	if x == y:
		same_count += 1
print(same_count)

# range: a sequence of consecutive integers
print(list(range(-2,2)))
print(list(range(4)))

def sum_below(n):
	total = 0
	for i in range(n):
		total += i
	return total
n = 10
print(sum_below(n))

# function tool to do this work
import functools
print(functools.reduce(lambda x,y: x+y, range(n)))


def cheer():
	for _ in range(3): # if not use the name
		print('go bears')

		
# list comprehensions
# use a list to compute a new list 
letters = ['a','b','c','d','e','f','m','n','o','p']
print([letters[i] for i in [3,4,6,8]])


odds = [1,3,5,7,9]
[x+1 for x in odds]
[x for x in odds if 25%x==0]


# high order sequence functions
## functions that perform list comprehensions
map()
filter()
functools.reduce()

functools.reduce(pow, [1,2,3,4], 2) # 16777216
pow(pow(pow(pow(2,1),2),3),4) # 16777216



