"""
lecture 22
sets
"""

# sets
# no duplicates
# unordered

s = {3,1,2,3,5}
s
3 in s
len(s)
s.union({1,5})
s.intersection({6,5,4,3})

# implementing sets
## membership testing
## union
## intersection
## adjoin

# sets as unordered sequence
class Link:
	empty = ()
	
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest
		
	def __getitem__(self, i):
		"""implicit recursive"""
		if i == 0:
			return self.first
		else:
			return self.rest[i-1] # will invoke the same __getitem__ method
			
	def __len__(self):
		"""implicit recursive"""
		return 1 + len(self.rest)
		
	def __repr__(self):
		if self.rest: # rest is not empty
			rest_str = ', '+ repr(self.rest)
		else:  # rest is empty
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)
		
def extend(s,t):
	"""
	return a link with elements of s followed by those of t
	"""
	if s is Link.empty:
		return t
	else:
		return Link(s.first, extend(s.rest, t))
		
def keep_if(s, filter_fn):
	"""
	a linked list
	"""
	if s is Link.empty:
		return s
	kept = keep_if(s.rest, filter_fn)
	if filter_fn(s.first):
		return Link(s.first, kept)
	else:
		return kept
	

## sets ##
def empty(s):
	return s is Link.empty

def set_contains(s, v):
	"""
	return whether set s contains value v
	Time: O(n) -> depends on 
	>>> s = Link(1, Link(2, Link(3)))
	>>> set_contains(s, 2)
	True
	"""
	if empty(s):
		return False
	elif s.first == v:
		return True
	else:
		return set_contains(s.rest, v)

def adjoin_set(s, v):
	if set_contains(s, v):
		return s
	else:
		return Link(v, s)

def intersect_set(set1, set2):
	"""
	
	"""
	'''
	# unordered version:
	# O(n^2)
	in_set2 = lambda v: set_contains(set2, v)
	return keep_if(set1, in_set2) # need a new version defined for link instances
	
	'''
	# ordered version
	# ordered from least to greatest
	# O(m+n)
	if empty(set1) or empty(set2):
		return Link.empty
	else:
		e1, e2 = set1.first, set2.first
		if e1 == e2:
			return Link(e1, intersect_set(set1.rest, set2.rest))
		elif e1 < e2:
			return intersect_set(set1.rest, set2)
		else:
			return intersect_set(set1, set2.rest)
			
	
def union_set(set1, set2):
	"""
	O(n^2)
	"""
	not_in_set2 = lambda v: not set_contains(set2, v)
	set1_not_set = keep_if(set1, not_in_set2)
	return extend(set1_not_set2, set2)
	
	

# sets as binary search trees
# a set is represented as a tree with two branches 
# each entry is: (1) larger than all entries in its left branch (2) smaller than all entries in its right branch

# idea: 
# fill the place of a missing left branch with an empty tree
# binary tree always has exactly two branches (leave has two empty children)
class Tree:
	def __init__(self, entry, branches=()):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree) # check if the branch is the instance of Tree
		self.branches = list(branches)
		
	def __repr__(self):
		if self.branches:
			branches_repr = ', '+repr(self.branches)
		else:
			branches_repr = ''
		return 'Tree({0}{1})'.format(self.entry, branches_repr)
		
		
class BinaryTree(Tree):
	empty = Tree(None)
	empty.is_empty = True
	
	def __init__(self, entry, left=empty, right=empty):
		Tree.__init__(self, entry, (left, right))
		self.is_empty = False
		
	@property
	def left(self):
		return self.branches[0]
		
	@property
	def right(self):
		return self.branches[1]

B = BinaryTree
t = B(3, B(1),
		 B(7))	# Tree(3, [Tree(1, [Tree(None), Tree(None)]), Tree(7, [Tree(None), Tree(None)])])


# membership in binary search trees
def set_contains(s, v):
	"""
	if s(linked list) contains v
	
	if the tree is roughly balanced 
	search time is O(logn)
	grows much slower than n 
	so binary search tree was used a lot 
	"""
	if s.is_empty:
		return False
	elif s.entry == v:
		return True
	elif s.entry < v:
		return set_contains(s.right, v)
	else:	# s.entry > v:
		return set_contains(s.left, v)
		
# adjoining to a tree set
def adjoin_set(s, v):
	"""
	return a set containing all elements of s and new element v
	"""
	if s.is_empty:
		return BinaryTree(v)
	elif s.entry == v:
		return s
	elif s.entry < v:
		return BinaryTree(s.entry, s.eft, adjoin_set(s.right, v))
	else: # s.entry > v:
		return BinaryTree(s.entry, adjoin_set(s.left, v), s.right)
	
		
