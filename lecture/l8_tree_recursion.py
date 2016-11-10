"""
lecture 8 
tree recursion


"""

# order of recursive calls 

# standard recursive version
def cascade_v1(n):
	if n < 10:
		print(n)  # print '4'
	else:
		print(n)  # print the first part before '4'
		cascade(n//10) # all but last digit
		print(n)  # print the second part after '4'
		
# n = 4589
'''
4589
458
45
4
45
458
4589
'''

# shorter version
def cascade_v2(n):
	print(n)  # print first: print the first part and '4' 
	if n > 10:
		cascade_v2(n//10)
		print(n) # print the second part after '4'
		
# n = 4589
'''
4589
458
45
4
45
458
4589
'''

# inverse_cascade(n):
def inverse_cascade(n):
	grown(n)
	print(n)
	shrink(n)
	
def f_then_g(f,g,n):
	if n:
		f(n)
		g(n)
		
grown = lambda n: f_then_g(grown, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)


inverse_cascade(12345)
'''
1
12
123
1234
12345
1234
123
12
1
'''




# tree recursion
# executing the body of a recursive function makes more than one call to that function


# not the best
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-2) + fib(n-1)  # lots of repeated calculation
		

# when use tree recursion -> exploring different choices		

# number partitions 
# def count_partitions(n, m)
# integer n -> using parts up to m (each part not greater than m)
# how many number of ways in which n can be expressed 

def count_partitions(n, m):
	"""
	explore two possibilities
	(1) use at least one m
	(2) don't use any m
	
	then solve two simpler problems -> recursion
	"""
	if n == 0:
		return 1  # par 0, only one way to do it
	elif n < 0:
		return 0  # no way to do this, wrong condition
	elif m == 0:
		return 0  # maximum size of m is 0 -> no way to do anything
	else:
		with_m = count_partitions(n-m, m)
		without_m = count_partitions(n, m-1)
		return with_m + without_m
		
result = count_partitions(5,3)
# without m -> count_partitions(5,2)
	# without m -> count_partitions(5,1)
		#...
	# with m -> count_partitions(3,2)
		#...
# with m -> count_partitions(2,3)
	# without m -> count_partitions(2,2)
		#...
	# with m -> count_partitions(1,3)
		#...

# 1+1+1+1+1=5
# 1+1+1+2=5
# 1+2+2=5
# 1+1+3=5
# 2+3=5


