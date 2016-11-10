"""
linked list structure 
using object 
"""

# linked list:
# either empty or a first value and the rest of the linked list
# a linked list is a pair 
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

def extend_link(s,t):
	"""
	return a link with elements of s followed by those of t
	"""
	if s is Link.empty:
		return t
	else:
		return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
	"""
	apply f to each element of s
	"""
	if s is Link.empty:
		return s
	else:
		return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
	"""
	return a link with elements of s for which f returns true
	"""
	if s is Link.empty:
		return s
	else:
		filtered = filter_link(f, s.rest)
		if f(s.first):
			return Link(s.first, filtered)
		else:
			return filtered

def join_link(s, separator='-'):
	"""
	return a string of all element in s separated by separator	
	"""
	if s is Link.empty:
		return ""
	elif s.rest is Link.empty:
		return str(s.first)
	else:
		return str(s.first) + separator + join_link(s.rest, separator)


		
s = Link(3, Link(4, Link(5)))
s.rest.first  # 4
s.rest.rest.rest is Link.empty  # True
s.rest.first = 7
s # Link(3, Link(7, Link(5)))
Link(8, s.rest) # Link(8, Link(7, Link(5)))
len(s) # 3
s[2]  # 5

extend_link(s, s) # Link(3, Link(7, Link(5, Link(3, Link(7, Link(5))))))

map_link(lambda x: x**2, s)  # Link(9, Link(49, Link(25)))

filter_link(lambda x: x%2==1, s) # Link(3, Link(7, Link(5)))

join_link(s) # '3-7-5'


# sequence operations
# __getitem__
# __len__
		
		
		
def partitions(n, m):
	if n == 0:
		return Link(Link.empty)
	if n < 0 or m ==0:
		return Link.empty
	else:
		using_m = partitions(n-m, m)
		with_m = map_link(lambda p: Link(m, p), using_m)
		without_m = partitions(n, m-1)
		return extend_link(with_m, without_m)
		
def print_partitions(n, m):
	"""
	print the partitions of n using parts up to size m
	"""
	links = partitions(n, m)
	lines = map_link(lambda s: join_link(s), links)
	
	map_link(print, lines)