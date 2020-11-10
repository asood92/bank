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
        if (self.balance - amount) < 0:
            self.balance -= 10
            print("\n Insufficient funds. Overdraft fee of $10 assessed. \n")
        else:
            self.balance -= amount

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
Anita = BankAccount("Anita Jenkins", 63144822, 212313414, 1202.78)
Molly = BankAccount("Molly Webb", 93146681, 212313414, 7203.65)

Jeff.print_receipt()
Jeff.deposit(312)
Jeff.print_receipt()

Anita.print_receipt()
Anita.withdraw(1288)
Anita.print_receipt()

Molly.print_receipt()
Molly.get_balance()
Molly.add_interest()
Molly.print_receipt()