import random
from colorama import init, Fore

init(autoreset=True)

computer_choice = ["rock", "paper", "scissors"]
random_choice = random.choice(computer_choice)
your_choice = str(input("Type rock, paper, or scissors: ")).lower()
if your_choice != "rock" and your_choice != "paper" and your_choice != "scissors":
    print("YOU CHOOSE WRONG, YOU LOSE")
elif your_choice == random_choice:
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.YELLOW + "It's a draw")
elif your_choice == "rock" and random_choice == "scissors":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.GREEN + "You win")
elif your_choice == "rock" and random_choice == "paper":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.RED + "You lost")
elif your_choice == "paper" and random_choice == "rock":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.GREEN + "You win")
elif your_choice == "paper" and random_choice == "scissors":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.RED + "You lost")
elif your_choice == "scissors" and random_choice == "paper":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.GREEN + "You win")
elif your_choice == "scissors" and random_choice == "rock":
    print("You choose: {} and the computer choose: {}".format(your_choice, random_choice))
    print(Fore.RED + "You lost")


