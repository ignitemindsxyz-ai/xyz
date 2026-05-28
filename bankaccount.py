class BankAccount:

    transactions = []

    def __init__(self, owner, transactions, balance):
        self.owner = owner
        self._transactions = transactions
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            balance += amount
            self._transactions.append(amount)

        else:
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self._transactions.append(-amount)

        else:
            raise ValueError ("Withdrawal must be positive and not exceed the current balance0")
        
    def get_balance(self):
        return self.__balance
    
    def __repr__(self):
        return f"Owner : {self.owner}, Balance : {self.__balance}"
    
acc1 = BankAccount("Bob", +100, 10000)
acc2 = BankAccount("Susan", -100, 2000)

print(acc1.owner)
print(acc2.owner)
print(acc1.get_balance())
print(acc2.get_balance())
print(acc1._transactions)
print(acc2._transactions)
print(acc1._BankAccount__balance)
print(acc2._BankAccount__balance)