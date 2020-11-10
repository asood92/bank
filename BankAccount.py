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
        if self.balance < 0:
            self.balance -= 10
            print("Insufficient funds. Overdraft fee of $10 assessed.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        safe_number = 0
        for number in self._account_number:
            safe_number = number[0:3] + "*"
        print(
            f"{self._full_name} \n Account No: {safe_number} \n Routing No: {self._routing_number} \n Balance: ${self.balance}"
        )


Jeff = BankAccount("Jeff Johns", 86753090, 212313414, 3025.33)
Anita = BankAccount("Anita Hill", 63144822, 212313414, 121302.78)
Molly = BankAccount("Molly Webb", 93146681, 212313414, 72803.65)

print(Jeff)
print(Anita)
print(Molly)