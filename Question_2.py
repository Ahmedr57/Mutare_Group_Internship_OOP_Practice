#1.	Write a class BankAccount with a constructor that initializes the account holder's name, account number, and initial balance. 
# Implement methods to deposit, withdraw, and display the current balance. 
# Ensure that the balance can never be accessed or modified directly from outside the class (use encapsulation).
class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount Deposited: {amount}")

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Amount Withdrawn: {amount}")

    def display_balance(self):
        print(f"Current Balance: {self.__balance}")

acc1 = BankAccount("Shahid ", 568932, 5000)
print(acc1.name)
acc1.display_balance()
acc1.deposit(40000)
acc1.display_balance()
acc1.withdraw(7800)
acc1.display_balance()


        
