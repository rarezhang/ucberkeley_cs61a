"""
Lecture 13
sequence 
"""

# linked lists
# a lined list is a pair
# the 0-indexed element of the pair is the first element of the linked list
# the 1-indexed element of the pair is the rest of the linked list

empty = 'empty'

def is_link(s):
	"""
	s is link:
	(1) empty or
	(2) (first, rest) pair
	"""
	return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1])) # recursive check
	

## constructor:
def link(first, rest):
	"""
	construct a linked list from its first element and the rest
	
	"""
	assert is_link(rest), 'rest must be a linked list'
	return [first, rest]

## selectors:
def first(s):
	"""
	return the first element of a linked list s
	"""
	assert is_link(s), 's is not a linked list'
	assert s != empty, 'empty linked list has no first element'
	return s[0]
	
def rest(s):
	"""
	return the rest of the elements of a linked list s
	"""
	assert is_link(s), 's is not a linked list'
	assert s != empty, 'empty lined list has no rest'
	return s[1]
	
def len_link(s):
	"""
	return the length of linked list
	"""
	"""
	# while version
	length = 0
	while s != empty:
		s, length = rest(s), length + 1
	return length
	"""
	if s == 'empty':
		return 0
	else:
		return 1 + len_link(rest(s))

def getitem_link(s, i):
	"""
	return the element at index i of linked list s
	"""
	"""	
	# while version
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)
	"""
	if i == 0:
		return first(s)
	else:
		return getitem_link(rest(s), i-1)
	

def extend(s, t):
	"""
	combine two linked lists
	return one single linked list
	"""
	assert is_link(s) and is_link(t), 's and t must be linked lists'
	if s == empty:
		return t
	else:
		return link(first(s), extend(rest(s), t))

def reverse(s):
	"""
	"""
	def reverse_to(s, t):
		"""
		"""
		if s == empty:
			return t
		else:
			return reverse_to(rest(s), link(first(s), t))
			
	return reverse_to(s, empty)
	

def apply_to_all_link(f, s):
	"""
	>>> s = [1, [2, 'empty']]
	>>> apply_to_all_link(lambda x: x**3, s)
	[1, [8, 'empty']]
	"""
	if s == empty:
		return empty
	else:
		return link(f(first(s)), apply_to_all_link(f,rest(s)))
		
		
# application of linked list
# partitions
# simpler version: l8_tree_recursion.py --> just count how many ways 
# here: return all the possibilities	

def partitions(n, m):
	"""
	return a linked list of the partitions of integer n using parts up to m
	each partition is a linked list of numbers
	"""
	if n == 0: # only one way to partition
		return link(empty, empty)
	elif n < 0: # no way to partition
		return empty
	elif m == 0: # no way to partition
		return empty
	else: # tree_recursion
		# do we use at lease one m?
		yes = partitions(n-m, m) # return a partition of (n-m), need to add a 'm' in the linked list
		add_m = lambda s: link(m, s)
		with_m = apply_to_all_link(add_m, yes)
		no = partitions(n, m-1)
		return extend(with_m, no)  # can get the correct result, but not easy to read

def join(s, separator='-'):
	"""
	join a linked list with given separator
	"""
	if s == empty:
		return ''
	elif rest(s) == empty:
		return str(first(s))
	else:
		return str(first(s)) + separator + join(rest(s), separator)
	
def print_partitions(n, m):
	links = partitions(n, m)  # get list of links 
	print(links)
	strings = apply_to_all_link(lambda s: join(s, ' + '), links)  # still a list of links, but each element is a string now
	print(strings)
	print(join(strings, '\n')) # separate partitions by a new line

######################################################################################
# rooted tree --> still linked list
# a tree has a root value and a sequence of branches (which are each rooted trees)
def rooted(value, branches):
	for branch in branches:
		assert is_rooted(branch)
	return [value] + list(branches)
	
def is_rooted(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_rooted(branch):
			return False
	return True

def root(tree):
	return tree[0]
	
def branches(tree):
	return tree[1:]
	
rooted(3, [rooted(1, []), rooted(2, [rooted(1,[]), rooted(1, [])])])
# [3, [1], [2, [1], [1]]]

# use rooted tree
def fib_tree(n):
	if n == 0 or n == 1:
		return rooted(n, [])
	else:
		left, right = fib_tree(n-2), fib_tree(n-1)
		root_value = root(left) + root(right)
		return rooted(root_value, [left, right])
	
fib_tree(5)
# [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]

def partition_tree(n, m):
	"""
	return a tree of the partitions of integer n using parts up to m
	"""
	if n==0:
		return rooted(True, [])
	elif n < 0:
		return rooted(False, [])
	elif m == 0:
		return rooted(False, [])
	else:
		yes = partition_tree(n-m, m)
		no = partition_tree(n,m-1)
		return rooted(m, [yes, no])  # hard to read
		
def print_partitions_tree(tree, partition=empty):
	if branches(tree) == [] and root(tree):
		print(join(partition, '+'))
	elif branches(tree):
		m = root(tree)
		left, right = branches(tree)
		print_partitions_tree(left, link(m, partition))
		print_partitions_tree(right, partition)

ptree = partition_tree(6,4)
print_partitions_tree(ptree)
"""
2+4
1+1+4
3+3
1+2+3
1+1+1+3
2+2+2
1+1+2+2
1+1+1+1+2
1+1+1+1+1+1
"""
	
# simple examples of linked list
# construct a linked list
link(1, empty)  # [1, 'empty']
link(1, link(2, empty))  # [1, [2, 'empty']]

s = link(1, link(2, empty)) 

four = link(1, link(2, link(3, link(4, empty))))
# [1, [2, [3, [4, 'empty']]]]
march = link(1, link(2, link(1, link(2, empty))))
# [1, [2, [1, [2, 'empty']]]]
both = link(march, link(four, empty))
# [[1, [2, [1, [2, 'empty']]]], [[1, [2, [3, [4, 'empty']]]], 'empty']]

first(rest(rest(first(rest(both)))))
# rest(both) -> [[1, [2, [3, [4, 'empty']]]], 'empty']
# first(rest(both)) -> [1, [2, [3, [4, 'empty']]]]
# rest(first(rest(both))) -> [2, [3, [4, 'empty']]]
# rest(rest(first(rest(both)))) -> [3, [4, 'empty']]
# first(rest(rest(first(rest(both))))) -> 3

first(rest(first(rest(rest(both)))))
# rest(both) -> [[1, [2, [3, [4, 'empty']]]], 'empty']
# rest(rest(both)) -> 'empty'
# first(rest(rest(both))) -> 'empty linked list has no first element'

first(rest(first(rest(first(both)))))
# first(both) -> [1, [2, [1, [2, 'empty']]]]
# rest(first(both)) -> [2, [1, [2, 'empty']]]
# first(rest(first(both))) -> 2
# rest(first(rest(first(both)))) -> 's is not a linked list'