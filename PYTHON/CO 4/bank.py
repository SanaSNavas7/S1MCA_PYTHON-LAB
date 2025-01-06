class Bank:
	def __init__(self,accno,name,typ,balance):
		self.accno=accno
		self.name=name
		self.typ=typ
		self.balance=balance
		
	def deposit(dep):
		amnt = int(input("Enter the amount to deposit : "))
		new_bal = dep.balance+amnt
		print("Your current status is ")
		print(dep.accno)
		print(dep.name)
		print(dep.typ)
		print("New balance is : " , new_bal)
		
	def withdraw(wtd):
		amnt = int(input("Enter the amount to withdraw : "))
		new_bal = wtd.balance-amnt
		print("Your current status is ")
		print(wtd.accno)
		print(wtd.name)
		print(wtd.typ)
		print("New balance is : " , new_bal)
		
		
accno = int(input("Enter the account number : "))
name = input("Enter the name : ")
typ = input("What is your account type? (Savings/Current) : ")
balance = int(input("Enter your current account balance : "))
print("What you need to perform?")
print("Enter 1 TO DEPOSIT")
print("Enter 2 to WITHDRAW")
choice = int(input())
acc = Bank(accno,name,typ,balance)
if choice == 1:
	acc.deposit()
elif choice == 2:
	acc.withdraw()
else:
	print("Invalid entry")

	
	
