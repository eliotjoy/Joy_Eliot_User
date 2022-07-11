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
    def enroll(self):
        if self.is_rewards_member == True:
            print("Already enrolled with", self.gold_card_points, "gold card points")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("Now enrolled with 200 gold card points")
    def spend_points(self, amount):
        if self.is_rewards_member == False:
            print("Not yet enrolled. Enroll as a rewards member to access gold card points.")
        elif self.is_rewards_member == True:
            if amount <= self.gold_card_points:
                self.gold_card_points -= amount
                print(self.gold_card_points, "gold card points remaining.")
            else:
                remainder = amount - self.gold_card_points
                print("Only", self.gold_card_points, "gold card points were left in account.")
                self.gold_card_points = 0
                print("Account now at 0. Unable to spend remaining", remainder, "points requested.")



user_1 = User("Ada", "Lovelace", "adalove@protonmail.org", 100)
user_1.display_info()

user_1.enroll()
print(user_1.is_rewards_member, user_1.gold_card_points)

user_2 = User("Coding", "Dojo", "codingdojo@aol.com", 25)
user_3 = User("Emperor", "Palpatine", "embracethehate@fu.net", 666)

user_1.spend_points(50)
print(user_1.gold_card_points)

user_2.enroll()
user_2.spend_points(80)

user_1.display_info()
user_2.display_info()
user_3.display_info()

user_1.enroll()

user_3.spend_points(40)
user_2.spend_points(200)