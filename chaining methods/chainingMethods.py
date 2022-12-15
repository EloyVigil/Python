class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self

user_1 = User("Mike", "Honcho", "spreadum@itwaswierd.com", 36)
user_2 = User("Austin", "Powers", "shaggin@thatsmybagbaby.com", 40)
user_3 = User("Rickey", "Bobby", "ifyourenotfirst@yourelast.com", 40)
user_1.enroll().display_info().spend_points(50)
user_2.enroll().display_info().spend_points(80)
user_3.enroll().display_info()
print(user_1.gold_card_points)
print(user_2.gold_card_points)