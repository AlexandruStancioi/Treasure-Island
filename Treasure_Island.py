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
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("CHAPTER 1")
print("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"  ---  " , end = "")
choice = input().lower()
if choice == "right" :
    print("\nCHAPTER 2")
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.  ---  " , end = "")
    choice = input().lower()
    if choice == "wait" :
        print("\nCHAPTER 3")
        print("You took a boat and arrived at the island unharmed. \nThere is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?  ---  " , end = "")
        choice = input().lower()
        if choice == "red":
            print("It's a room full of fire.\nxxx GAME OVER! xxx")
        if choice == "blue":
            print("You enter a room of beasts.\nxxx GAME OVER! xxx")
        if choice == "yellow":
            print("You found the treasure!\nYOU WIN !")
        else:
            print("You have chosen a door that doesn't exist.\nxxx GAME OVER! xxx")
    else :
        print("The lake was full of crocodiles.\nxxxxx GAME OVER! xxxxx")
else :
    print("\nYou fell into a hole.\nxxxxx GAME OVER! xxxxx")


