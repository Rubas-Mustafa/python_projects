# import random
# define a function to roll a dice 
#   create a dict for dice
# while loop 
# ranint means random integer

import random

def dice_roll():

    drawings = {
         1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }

    roll = input("Do you wanna roll it now: ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        #print("Dice Rolled: " + str(dice1) +"and" + str(dice2))
        print("Dice Rolled: {} and {}".format(dice1, dice2))
        print("".join(drawings[dice1]))
        print("".join(drawings[dice2]))
        
        roll = input("Again?????: ")

dice_roll()