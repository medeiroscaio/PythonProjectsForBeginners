logo= '''
                                        __  .__                                 ___.                 
   ____  __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
 / /_/  >  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \___  /|____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
/_____/             \/     \/     \/             \/     \/       \/            \/    \/     \/       

'''
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
number_chosen = random.choice(numbers)
user_number = 0
print(logo)
option = str(input("Choose 'easy' or 'hard': "))
option = option.lower()

life_easy = 10
life_hard = 5

def guess():
    global life_easy, life_hard
    if user_number == number_chosen:
        print("You guessed it!")
        print(f"The Guesse number are {number_chosen}")
    elif option == "easy" and user_number != number_chosen:
        life_easy -= 1
        print(f"Attempts: {life_easy}")
        if life_easy == 0:
            print("You Lost")
            print(f"The Guesse number are {number_chosen}")
    elif option == "hard" and user_number != number_chosen:
        life_hard -= 1
        print(f"Attempts: {life_hard}")
        if life_hard == 0:
            print("You Lost")
            print(f"The Guesse number are {number_chosen}")
def close_the_number():
    if user_number > number_chosen:
        print("Too High")
    elif user_number < number_chosen:
        print("Too low")

while user_number != number_chosen and life_easy != 0 and life_hard != 0:
    print()
    user_number = int(input("Guess the number: "))
    guess()
    close_the_number()

