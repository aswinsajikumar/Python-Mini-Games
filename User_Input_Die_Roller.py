import random


def roll(die, sides): 
    r = 0  
    while r < die:  
        rolls = random.randint(1, sides)  
        r += 1  
        print("You Rolled a", rolls)  


def main():  
    rolling = True 
    while rolling:  
        answer = input("Ready to roll? Y or N: ") 
        if answer.lower() == "y": 
            die = int(input("Please enter the number of dice you wish to roll: ")) 
            sides = int(input("Please enter the number of sides on your dice: "))  
            roll(die, sides) 
        elif answer.lower() == "n": 
            print("Thank you for playing!")
            break
        else:
            print("Invalid Input")
            


main()  
