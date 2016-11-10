"""
lecture 14 object oriented programming
"""

# object oriented programming
# method for organizing modular programs

## abstraction barriers
## bundling together data and behavior

# classes
## template for its instances

class Account:
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
		
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance
		
	def withdraw(self, amount):
		if amount > slef.banlance:
			return 'insufficient funds'
		self.balance = self.balance - amount
		return self.balance
		
Jim = Account('Jim')



