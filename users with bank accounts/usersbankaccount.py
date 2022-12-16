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


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.savings = BankAccount(0.06, 20000)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

    def make_withdraw(self, amount):
        self.savings.withdraw(amount)
        return self

    def display_user_balance(self):
        self.savings.display_account_info()
        return self




user_1 = User("Mike", "Honcho", "spreadum@itwaswierd.com", 36)
user_2 = User("Austin", "Powers", "shaggin@thatsmybagbaby.com", 40)
user_3 = User("Rickey", "Bobby", "ifyourenotfirst@yourelast.com", 40)

user_1.make_withdraw(1000).display_user_balance()
