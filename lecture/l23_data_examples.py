"""
Lecture 23 
data example
"""

# mutable linked list
class Link:
	"""
	a linked list
	"""
	empty = ()
	
	def __init__(self, first, rest=empty):
		self.first = first
		self.rest = rest
	
	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]
			
	def __len__(self):
		return 1 + len(self.rest)
		
	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)
	
	
# recursive lists can change 
s = Link(1, Link(2, Link(3)))
# s-> Link(1, Link(2, Link(3)))
s.first = 5
# s-> Link(5, Link(2, Link(3)))
t = s.rest
# s-> Link(5, Link(2, Link(3)))
# s-> Link(5, t)
# t-> Link(2, Link(3))
t.rest = s
# loop: cannot print out s and t
# s = Link(5, t=Link(2, s))
s.first
# 5
s.rest.rest.rest.rest.rest.first
# s.rest = Link(2, s)
# s.rest.rest = Link(5, t=Link(2, s))
# s.rest.rest.rest = Link(2, s)
# s.rest.rest.rest.rest = Link(5, t=Link(2, s))
# s.rest.rest.rest.rest.rest = Link(2, s)
# s.rest.rest.rest.rest.rest.first = 2




####################################
# environment digram

def oski(bear):
	def cal(berk):
		nonlocal bear
		if bear(berk) == 0:
			return [berk+1, berk-1]
		bear = lambda ley: berk - ley
		return [berk, cal(berk)]
	return cal(2)
	
oski(abs) # [2, [3, 1]]
'''
- global:
oski(bear) [p=g]

- f1:
nonlocal bear = abs  -> bear = lambda ley: berk - ley
cal(2)
return xxx

- f2:
cal(2) [p=f1]
berk = 2
nonlocal bear = lambda ley: berk - ley
return [berk=2, cal(berk)]

- f3:
cal(berk) [p=f1]

- f4:
lambda ley: berk - ley [p=f2]
ley = 2
return [berk+1, berk-1] = [3, 1]

combine f3,f1 --> return [2, [3, 1]]

'''

# objects system 

# instance attributes are found before class attributes 
# class attributes are inherited

# land owners example
class Worker:
	greeting = 'Sir'
	def __init__(self):
		self.elf = Worker
	def work(self):
		return self.greeting + ', I work'
	def __repr__(self):
		return Bourgeoisie.greeting
		
class Bourgeoisie(Worker):
	greeting = 'Peon'
	def work(self):
		print(Worker.work(self))
		return 'I gather wealth'
		
jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

'''
- class Worker
greeting = 'Sir'
elf
work()
__repr__

- class Bourgeoisie
greeting = 'Peon'
work()

- object jack -> class Worker
greeting = 'Maam'

- object john -> class Bourgeoisie
'''

Worker().work()
# 'Sir, I work'
jack
# object jack -> class Worker -> __repr__ -> return Bourgeoisie.greeting
# Peon
jack.work()
# object jack (self.greeting ='Maam') -> class Worker -> work() -> return self.greeting + ', I work'
# 'Maam, I work'
john.work()
# object john -> class Bourgeoisie -> print(Wroker.work(self)) 		return 'I gather wealth'
# Wroker.work(self) -> return self.greeting + ', I work'
# Peon, I work   -> since print, so no ''
# return 'I gather wealth'
# 'I gather wealth'
john.elf.work(john)
# object john -> class Bourgeoisie
# elf = Worker
# john.elf -> john.Worker
# Worker.work(john) -> self.greeting ('Peon') + ', I work'
# 'Peon, I work'


###########################
# Binary Trees
# Morse Code
# signaling protocol that transmits messages by sequences of signals
# builds a tree -> def morse
# def decode -> get correct 

abcde = {'a':'.-', 'b':'-...','c':'-.-.','d':'-..','e':'.'}
	
def decode(signals, tree):
	"""
	decode signals into a letter using a morse code tree
	"""
	for signal in signals:
		if signal == '.':
			tree = tree.left
		elif signal == '-':
			tree = tree.right
	return tree.entry
	
class Tree:
	"""
	a tree with entry as its root value
	"""
	def __init__(self, entry, branches=()):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)
		
	def __repr__(self):
		if self.branches:
			branches_str = ', ' + repr(self.branches)
		else:
			branches_str = ''
		return 'Tree({0}{1})'.format(self.entry, branches_str)
		
	def is_leaf(self):
		return not self.branches
		
class BinaryTree(Tree):
	"""
	a tree with exactly two branches, which may be empty
	"""
	empty = Tree(None)
	empty.is_empty = True
	
	def __init__(self, entry, left=empty, right=empty):
		for branch in (left, right):
			assert isinstance(branch, BinaryTree) or branch.is_empty
		Tree.__init__(self, entry, (left, right))
		self.is_empty = False
		
	@property
	def left(self):
		return self.branches[0]
		
	@property
	def right(self):
		return self.branches[1]
'''		
	def __repr__(self):
		if self.left.is_empty and self.right.is_empty:
			return 'BinaryTree({0})'.format(self.entry)
		elif self.right.is_empty:
'''

def morse(code):
	"""
	return a binary tree representing the code
	"""
	root = BinaryTree(' ')
	for letter, signals in code.items():
		tree = root
		# traverse the tree
		for signal in signals:
			if signal == '.':
				tree = ensure(tree, 0)
			elif signal == '-':
				tree = ensure(tree, 1)
		tree.entry = letter
	return root	

	
def ensure(tree, k):
	if tree.branches[k] is BinaryTree.empty:
		tree.branches[k] = BinaryTree(' ')
	return tree.branches[k]
	
morse(abcde)
'''
Tree( , [Tree(e, [Tree(None), Tree(a, [Tree(None), Tree(None)])]), Tree( , [Tree( , [Tree(d, [Tree(b, [Tree(None), Tree(None)]), Tree(None)]), Tree( , [Tree(c, [Tree(None), Tree(None)]), Tree(None)])]), Tree(None)])])
'''	

decode('-.-.', morse(abcde))
# 'c'
		