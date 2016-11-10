"""
lecture 13
mutable function
function has data associated with them (--> the data changes)
"""

# example
# mutable function 
# function with behaviour that varies over time

# model a bank account that has a balance of $100

# def make_withdraw -> create bank account
# def withdraw -> calling make_withdraw, with para balance


def make_withdraw(balance):
	"""
	return a withdraw function with a starting balance
	"""
	def withdraw(amount):
		# declare the name 'balance' nonlocal at the top of body of the function in which it is re-assigned
		nonlocal balance # nonlocal change of the value of balance will happen in the frame of make_withdraw !!!
		if amount > balance:
			return 'insufficient funds'
		balance = balance - amount # rebind balance in the first non-local frame in which it was bound previously
		return balance 
	return withdraw
	
wd = make_withdraw(100) # return the withdraw() function
print(wd(50))  # withdraw(amount) -> with parameter amount -> return 100-50=50
print(wd(20))  # return 50-20=30

# multiple mutable functions
john = make_withdraw(100)
steven = make_withdraw(1000)
john == steven  # false, even if steven = 100


		
