import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
life=6
end_of_game = False
display = []
word_list = ["Apple", "Banana", "Orange", "Strawberry", "Pineapple", "Grape", "Peach", "Mango", "Watermelon", "Kiwi"]
chosen_word = random.choice(word_list)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
for _ in chosen_word:
    display += "_"
print(logo)
print()
print(stages[6])
while not end_of_game:
    guess = str(input("Guess a letter: ")).lower()
    if guess in display:
        print("You already chose this letter")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if "_" not in display:
        end_of_game = True

    if guess not in chosen_word:
        life -= 1
        print("Wrong Letter")
    if life == 5:
        print(stages[5])
    elif life == 4:
        print(stages[4])
    elif life == 3:
        print(stages[3])
    elif life == 2:
        print(stages[2])
    elif life == 1:
        print(stages[1])
    elif life == 0:
        print(stages[0])
    if life == 0:
        end_of_game = True
        print("You Lost")
        print(chosen_word)


    print(display)










