class BankAccount:
    def __init__(self, name, startbalance=0):
        self.name = name
        self.__balance = startbalance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError(f'Unsufficient funds -- current balance: {str(self.__balance)}')

    @property
    def balance(self):
        return self.__balance

    def __repr__(self):
        return f'This is the Bank Account of {self.name}'
