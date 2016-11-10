"""
lecture 20
measuring efficiency
"""

# recursive computation of the fibonacci sequence

def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-2) + fib(n-1)

def count(f):
	def counted(n):
		counted.call_count += 1
		return f(n)
	counted.call_count = 0
	return counted
'''	
fib = count(fib)
fib(5)
fib.call_count	 # 15
'''

# memoization
# remember the results that have been computed before
def memo(f):
	# keep the cache of the function returns before
	cache = {} # keys are arguments thaht map to return values
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized  # if f() is a ``pure function``, this decorator's behaviour will just like f()
'''
## speed up fib()

fib = count(fib)
counted_fib = fib
counted_fib(30)
counted_fib.call_count  # 2692537

fib = memo(fib)
fib = count(fib)
fib(30)
fib.call_count  # 59
'''


# Tree Class
# has an entry at its root and a list of branches

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
@memo
def fib_tree(n):
	if n == 0 or n == 1:
		return Tree(n)
	else:
		left = fib_tree(n-2)
		right = fib_tree(n-1)
		return Tree(left.entry + right.entry, [left, right])
		

		
# hailstone trees
# pick a positive integer n as the start
# if n is even, divide it by 2
# if n is odd, multiply it by 3 and add 1
# continue this process until n is 1

def hailstone(n):
	"""
	one way to print hailstone
	return the length of hailstone
	"""
	print(n)
	if n == 1:
		return 1 # return the total length 
	elif n % 2 == 0:
		return 1 + hailstone(n//2)
	else:
		return 1 + hailstone(n*3+1)

# using trees
def is_int(x):
	return int(x) == x
	
def is_odd(x):
	return x % 2 == 1

def hailstone_tree(k, n=1):
	if k == 1:
		return Tree(n)
	else:
		branches = []
		branches.append(hailstone_tree(k-1, n*2))
		less = (n-1)/3
		if less > 1 and is_int(less) and is_odd(less): # bug
			branches.append(hailstone_tree(k-1, int(less)))
		return Tree(n, branches)
		
def leaves(t):
	"""
	take a tree t 
	return all the leaves of the tree
	>>> leaves(hailstone_tree(8))
	[128, 21, 20, 3]
	"""
	if not t.branches:
		return [t.entry]
	else:
		return sum([leaves(b) for b in t.branches], []) # sum(,[]) --> join list of lists into one list
	
def longest_path_below(k, t):
	"""
	find the longest path of hailstone tree: t
	the number never goes above some threshold value: k
	>>> longest_path_below(20, hailstone_tree(10))
	[1, 2, 4, 8, 16, 5, 10, 3, 6, 12]
	>>> longest_path_below(100, hailstone_tree(30))
	>>> [1, 2, 4, 8, 16, 5, 10, 20, 40, 13, 26, 52, 17, 34, 11, 22, 44, 88, 29, 58, 19, 38, 76, 25, 50]
	"""
	if t.entry >= k:
		return []
	elif not t.branches:
		return [t.entry]
	else:
		paths = [longest_path_below(k, b) for b in t.branches]
		return [t.entry] + max(paths, key=len)
		
		


		