print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_pass=str(input("\n You are at cross road. Where do you want to go?\n Choose 'left' or 'right' \n type: "))
lowerfirst_pass=first_pass.lower()
if lowerfirst_pass == "left":
    second_pass=str(input("You come to a lake, there is an island in the middle of lake. \n Choose 'wait' to wait the boat or 'swim' to swim \n type:  "))
    lowersecond_pass = second_pass.lower()
    if lowersecond_pass == "wait":
          third_pass=str(input("You arrive at the island unharmed. There is a house with 3 doors. \nRed \nBlue \nYellow \nWhich colour do you choose? "))
          lowerthird_pass=third_pass.lower()

          if lowerthird_pass == "red":
               print("Burned by fire \n GAME OVER")
          elif lowerthird_pass == "blue":
               print("Eaten by beasts \n GAME OVER")
          elif lowerthird_pass == "yellow":
              print("You find the treausure \n YOU WIN")
          else:
              print("Invalid door")

    elif lowersecond_pass == "swim":
        print("Attacked by trout. \n GAME OVER ")
    else:
        print("Invalid Option \n GAME OVER")
elif lowerfirst_pass == "right":
    print("Fall into a hole \n GAME OVER")
else:
    print("Invalid path \n GAME OVER")