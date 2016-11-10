"""
lecture 15 
inheritance
"""

# inheritance
# relating classes together 
# similar classes differ in their degree of specialization

## class <name>(<base class>)

# example: checking account is a specialized type of account

class Account:
	interest = 0.04
	
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
		
	def deposit(self, amount):
		self.balance = self.balance + amount
		return self.balance
		
	def withdraw(self, amount):
		if amount > self.balance:
			return 'insufficient funds'
		self.balance = self.balance - amount
		return self.balance
		

class CheckingAccount(Account):
	withdraw_fee = 1
	interest = 0.01
	
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_fee)

ch = CheckingAccount('Tom') # calls Account.__init__
print(ch.interest)  # can be found in CheckingAccount class
print(ch.deposit(20))  # can be found in Account class
print(ch.withdraw(5))  # can be found in CheckingAccount class