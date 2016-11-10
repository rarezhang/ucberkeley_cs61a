"""
Lecture 12
Trees
"""

# closure property of data types
## method (combining data values) has 'closure property' --> the result can be combined by the same method
## why important --> create hierarchical structures (made up of parts; parts are made up of parts)

# trees
# tree (1) leaf (2) a sequence of trees

# tree processing use recursion
## base case: processing a leaf
## recursive case: call on each branch 
## aggregates

tree = [[1,[2],3,[]],[[4],[5,6]],7]

def is_leaf(tree):
	return type(tree) != list
	
def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		branch_counts = [count_leaves(b) for b in tree]  # b: each branch
		return sum(branch_counts)
		
print(count_leaves(tree))


# flatten a tree
## how to use sum()
items = [[1],[2,3],[4]]
sum(items,[]) 
# [1, 2, 3, 4]
items = [[[1]],[2]]
sum(items, [])
# [[1], 2]

def flatten(tree):
	"""
	return a list containing the leaves of tree
	>>> flatten(tree)
	[1, 2, 3, 4, 5, 6, 7]
	"""
	if is_leaf(tree):
		return [tree]
	else:
		branch = [flatten(b) for b in tree]
		return sum(branch, [])
		
# membership & slicing
digits = [1,2,3]
print(2 in digits) # True

digits[1:]

# binary tree
# (1) leaf (2) at most two binary trees
def right_binarize(tree):
	"""
	construct a right_branching binary tree
	>>> right_binarize([1, 2, 3, 4, 5, 6, 7])
	[1, [2, [3, [4, [5, [6, 7]]]]]]
	"""
	if is_leaf(tree):
		return tree
	if len(tree) > 2:
		tree = [tree[0], tree[1:]] # all but the first branch are grouped into a new branch
	return [right_binarize(b) for b in tree]
	
pangram = [['the', 'quick', 'brown', 'fox'], ['jumps', 'over', 'a', 'lazy', 'dog']]
print(right_binarize(pangram))
# [['the', ['quick', ['brown', 'fox']]], ['jumps', ['over', ['a', ['lazy', 'dog']]]]]	


# strings
s = 'curry = lambda f: lambda x: lambda y: f(x, y)'
print(type(s), s)
#<class 'str'> curry = lambda f: lambda x: lambda y: f(x, y)
exec(s)  # execute the string
print(type(curry), curry)
#<class 'function'> <function <lambda> at 0x00>
from operator import add
re = curry(add)(3)(4)
print(re) # 7
	

# dictionary
# don't have an order !
n = {'i':1, 'v':5, 'x':10}
print(n.keys())	
print(n.values())
print(n.items()) # list of tuple
i = n.items()
nn = dict(i) # list of tuple -> dictionary
print(nn)
# check if a key is in a dictionary
print('x' in n) # True

n.get('x', 0) # return 10, 'x' is a key 
n.get('a', 0) # return 0, 'a' is not a key

# dictionary composition
{x: x*x for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
