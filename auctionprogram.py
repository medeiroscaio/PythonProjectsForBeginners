import os

users = []


def add_new_user(name, bid):
    users.append({"name": name, "bid": bid})


print("WELCOME TO AUCTION PROGRAM")
name = input("What's your name? ")
bid = int(input("Tell me your bid: $"))
add_new_user(name, bid)
os.system('cls')

max_bid = bid

game = True
while game:
    start = input("Do you want to 'add' more or 'stop'? ")
    if start == 'add':
        name = input("What's your name? ")
        bid = int(input("Tell me your bid: $"))
        add_new_user(name, bid)
        os.system('cls')

        if bid > max_bid:
            max_bid = bid

    elif start == 'stop':
        game = False

print("Users:")
for user in users:
    print(f"Name: {user['name']}, Bid: {user['bid']}")

print(f"Max Bid: {max_bid}")











