# class User:
#     def __init__(self, first, last):
#         self.first=first
#         self.last=last
#         self.account_balance = 0
#     # add deposit method
#     def make_deposit(self, amount): # takes an argument that is the amount of the deposit
#         self.account_balance += amount # the specific user's account increases by the amount of the value received

#     def make_withdrawl(self, amount):
#         self.account_balance -= amount

#     def display_user_balance(self):
#         print(f"User: {self.first}, Balance: ${self.account_balance}")
    
#     def transfer_money(self, other_user, amount):
#         other_user.make_deposit(amount)
#         self.make_withdrawl(amount)

# first_user=User("Steph", "Curry")
# second_user=User("LeBron", "Jame")
# third_user=User("Kobe", "Bryant")

# first_user.make_deposit(100000)
# first_user.make_deposit(500000)
# first_user.make_deposit(250000)
# first_user.make_withdrawl(50000)
# first_user.display_user_balance()

# second_user.make_deposit(20000)
# second_user.make_deposit(3000)
# second_user.make_deposit(4000)
# second_user.make_withdrawl(1000)
# second_user.display_user_balance()

# third_user.make_deposit(500000)
# third_user.make_deposit(200000)
# third_user.make_deposit(400000)
# third_user.make_withdrawl(60000)
# third_user.display_user_balance()

# # #BONUS
# third_user.transfer_money(first_user,50000)
# third_user.display_user_balance()
# first_user.display_user_balance()

