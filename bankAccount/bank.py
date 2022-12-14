class BankAccount:
    
    def __init__(self, interest, balance): 
        self.interest_rate = interest
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount> self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(self.balance, self.interest_rate)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.interest_rate
        return self

account1 = BankAccount(0.03, 67940.50)
account2 = BankAccount(0.1, 129834)

account1.deposit(3029).deposit(55).deposit(654.50).withdraw(1299).yield_interest().display_account_info()
account2.deposit(10456).deposit(679).withdraw(55.5).withdraw(300).withdraw(750).withdraw(342).yield_interest().display_account_info()