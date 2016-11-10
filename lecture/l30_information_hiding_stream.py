"""
lecture 30
information hiding

"""

# attributes for internal use 
# _ : one underscore is not meant to be referenced externally
# __: two underscore enforces restricted access from outside the class
# not accessible to other environments, except those that extend the frame
class FibIter:
	"""
	an iterator over fibonacci numbers
	"""
	def __init__(self):
		self._next = 0  # _next just for internal use
		self._addend = 1 # _addend just for internal use
		
	def __next__(self):
		result = self._next
		self._addend. self._next = self._next, self._addend+self._next
		
		
# singleton objects
# only ever has one instance
# e.g., NoneType -> none is its only instance

class empty_iterator:
	"""
	an iterator over no values
	"""
	def __next__(self):
		raise StopIteration

## user-defined singletons
# re-bind the class name to the instance
empty_iterator = empty_iterator()



# streams
# lazy linked lists (the rest of the list is computed on demand)

## Link(<first element>,<a link instance / Link.empty>)
## Stream(<first element>,<zero-argument function that returns a Stream / Steam.empty>)
# link and stream are interchangeable

# Streams
class Stream:
	"""
	a lazily computed linked list.
	a recursive list with an explicit first element and a rest of the list that is computed lazily.
	
	>>> s = Stream(1, lambda: Stream(6-2, lambda: Stream(9)))
	>>> s.first
	1
	>>> s.rest.first
	4
	>>> s.rest
	Stream(4, <...>)
	>>> s.rest.rest.first
	9
	"""
	class empty:
		def __repr__(self):
			return 'Stream.empty'
			
	empty = empty()
	
	def __init__(self, first, compute_rest=lambda: Stream.empty):
		assert callable(compute_rest), 'compute_rest must be calable'
		self.first = first
		self._compute_rest = compute_rest # _compute_rest: just for internal use
		
	@property
	def rest(self):
		"""
		return the rest of the stream, computing it if necessary
		"""
		if self._compute_rest is not None:
			self._rest = self._compute_rest()
			self._compute_rest = None
		return self._rest
		
	def __repr__(self):
		return 'Stream({0}, <...>)'.format(repr(self.first))


def first_k(s, k):
	"""
	return up to k elements of stream s as a list
	>>> s = Stream(1, lambda: Stream(4, lambda: Stream(9)))
	>>> first_k(s, 2)
	[1, 4]
	>>> first_k(s, 5)
	[1, 4, 9]
	"""
	elements = []
	while s is not Stream.empty and k>0:
		elements.append(s.first)
		s, k = s.rest, k-1
	return elements
	
	
def integer_stream(first):
	def compute_rest():
		return integer_stream(first+1)
	return Stream(first, compute_rest)
	
ints = integer_stream(1)
ints.first  # 1
ints.rest.first # 2
ints.rest # Stream(2, <...>)
first_k(ints, 10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square_stream(s):
	squared = s.first * s.first
	return Stream(squared, lambda: square_stream(s.rest))
	
s = integer_stream(1)
first_k(s, 10)
ss = square_stream(s)
first_k(ss, 10)


def add_streams(s, t):
	added = s.first + t.first
	def compute_rest():
		return add_streams(s.rest, t.rest)
	return Stream(added, compute_rest)
		
first_k(add_streams(s, s.rest), 10) # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]


# mapping a function over a Stream
# applies a function only to the first element; the rest is computed lazily
def map_stream(fn, s):
	"""
	map a function fn over the elements of a stream s
	"""
	if s is Stream.empty:
		return s
	def compute_rest():
		return map_stream(fn, s.rest)
	return Stream(fn(s.first), compute_rest)

# filtering a stream
# processing continues until an element is kept in the output 
def filter_stream(fn, s):
	"""
	filter stream s with predicate function fn
	"""
	if s is Stream.empty:
		return s
	def compute_rest():
		return filter_stream(fn, s.rest)
	
	if fn(s.first):
		return Stream(s.first, compute_rest)
	else:
		return compute_rest()
		
		
# stream of primes
# the stream of integers not divisble by any k<= n

def primes(s):
	"""
	returns stream
	takes a stream, already been filtered -> for any integers that are multiples of anything less than the first element in s
	"""
	def not_divisible(k):
		return k % s.first != 0
	
	def compute_rest():
		return primes(filter_stream(not_divisible, s))
		
	return Stream(s.first, compute_rest)
	
p = primes(integer_stream(2))
p.first # 2
p.rest.first # 3
p.rest.rest.first # 5
first_k(p, 10) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
	
