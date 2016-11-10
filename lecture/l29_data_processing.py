"""
lecture 29
data processing
"""

# processing sequential data
# big data processing 
## implicit representations of streams of sequential data
## declarative programming languages to manipulate and transform data
## distributed and parallel computing

# implicit sequences
# representation of the sequential data that not explicitly store each element

class Range:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		
	def __len__(self):
		return max(0,self.end - self.start)
		
	def __getitem(self, k):
		if k < 0:
			k = len(self) + k
		if k >= len(self):
			raise IndexError
		return self.start + k
		
	def __repr__(self):
		return 'Range({0},{1})'.format(self.start, self.end)

x = range(-2,2);
y = Range(-2,2)

# iterator interface 
# object that can provide the next element of a sequence
# __next__ : returns the next element
x = range(-2,2)

xi = iter(x)
xi.__next__()

class RangeIter:
	def __init__(self, start, end):
		self.next = start
		self.end = end
		
	def __next__(self):
		if self.next >= self.end:
			raise StopIteration
		result = self.next
		self.next += 1
		return result
		
y = Range(-2,2)
yi = RangeIter(-2,2)
next(yi)

# iterable objects
class LetterIter:
	def __init__(self, start='a', end='e'):
		self.next_letter = start
		self.end = end
		
	def __next__(self):
		if self.next_letter >= self.end:
			raise StopIteration
		result = self.next_letter
		print(result)
		self.next_letter = chr(ord(result)+1)
		return result

b_to_e = LetterIter('b', 'e')
next(b_to_e)

class Letters:
	def __init__(self, start='a', end='e'):
		self.start = start
		self.end = end
	
	def __iter__(self):
		return LetterIter(self.start, self.end)
		
s = Letters()
si = iter(s)
'''
next(si) -> 'a'
next(si) -> 'b'
next(si) -> 'c'
next(si) -> 'd'
next(si) -> StopIteration
'''
sj = iter(s)

# iterators from built-in functions
# generate result till that information is actually needed -> lazy computation
'''
map() # iterator over func(x) for x in iterable
filter() # iterate over x in iterable if func(x)
zip() # iterate over co-indexed (x,y) pars
reversed() # iterate over xi in a sequence in reverse order

# |#
#\/#
list() # create a list containing all x in iterable 
tuple() # create a tuple containing all x in iterable
sorted() # create a sorted list containing x in iterable
'''
b_to_e = Letters('b','r')
caps = map(lambda x: x.upper(), b_to_e)
caps

# generator function 
# iterator: created by a generator function
# yields values instead of returning them
# generator function yields multiple times

def letters_generator(next_letter, end):
	while next_letter < end:
		yield next_letter
		next_letter = chr(ord(next_letter)+1)


s = letters_generator('a','e')
list(letters_generator('a','e'))  # ['a', 'b', 'c', 'd']
next(s)
for l in s:
	print(l)
