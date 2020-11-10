class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self._full_name = full_name
        self._account_number = account_number
        self._routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\n Amount deposited: ${self.balance} \n")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 10
            print("\n Insufficient funds. Overdraft fee of $10 assessed. \n")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        obfuscation_string = "****"
        safe_number = str(self._account_number)
        safe_number = obfuscation_string + safe_number[4:]
        print(
            f"\n {self._full_name} \n Account No: {safe_number} \n Routing No: {self._routing_number} \n Balance: ${self.balance} \n",
        )


Jeff = BankAccount("Jeff Johns", 86753090, 212313414, 3025.33)
Anita = BankAccount("Anita Hill", 63144822, 212313414, 121302.78)
Molly = BankAccount("Molly Webb", 93146681, 212313414, 72803.65)

Jeff.deposit(312)
Jeff.print_receipt()

Anita.withdraw(6868)
Anita.print_receipt()

Anita.add_interest()
Anita.print_receipt()

Molly.get_balance()