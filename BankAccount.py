class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if (self.balance  < 0):
            self.balance -= 10
            print("Insufficient funds. Overdraft fee of $10 assessed.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def
