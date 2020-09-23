import random


def main():
    """Runs the entire game"""
    miles_traveled = 0
    thirst = 0
    hippogriff_tiredness = 0
    dementors_miles_traveled = -20
    canteen_drinks = 3
    done = False

    """Prints instructions for the game"""
    print("Welcome to the Wizarding World of Harry Potter!")
    print()
    print("You have stolen a hippogriff to help Sirius Black escape to a safe house.")
    print("The dementors want him back and are chasing you down! Survive your")
    print("trek and outrun the dementors!")
    print()

    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            """User chose to quit the game"""
            done = True
            print("You quit")

        elif user_choice.upper() == "E":
            """User chose to get a status check"""
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            print("The dementors are", (miles_traveled - dementors_miles_traveled), "miles behind you.")
            print()

        elif user_choice.upper() == "D":
            """User chose to stop for the night"""
            hippogriff_tiredness = 0
            dementors_miles_traveled += random.randrange(7, 21)
            print("The hippogriff is happy!")
            print()

        elif user_choice.upper() == "C":
            """User chose to fly full speed"""
            miles_traveled += random.randrange(10, 26)
            print("You traveled", miles_traveled, "miles")
            print()
            thirst += 1
            hippogriff_tiredness += random.randrange(1, 4)
            dementors_miles_traveled += random.randrange(7, 21)

            if random.randrange(20) == 0:
                """1 in 20 chance of running into Hagrid"""
                print("You have ran into Hagrid!")
                print("He has refilled your canteen and switched out your hippogriff!")
                print()
                canteen_drinks += 3
                thirst = 0
                hippogriff_tiredness = 0

        elif user_choice.upper() == "B":
            """User chose to fly at a moderate speed"""
            miles_traveled += random.randrange(5, 18)
            print("You traveled", miles_traveled, "miles")
            print()
            thirst += 1
            hippogriff_tiredness += 1
            dementors_miles_traveled += random.randrange(7, 21)

            if random.randrange(20) == 0:
                """1 in 20 chance of running into Hagrid"""
                print("You have ran into Hagrid")
                print("He has refilled your canteen and switched out your hippogriff!")
                print()
                canteen_drinks += 3
                thirst = 0
                hippogriff_tiredness = 0

        elif user_choice.upper() == "A":
            """User chose to drink from their canteen"""
            if canteen_drinks > 0:
                canteen_drinks -= 1
                thirst = 0
            else:
                print("You ran out of drinks!")
                print()

        if dementors_miles_traveled >= miles_traveled and not done:
            print("You have been caught by the dementors!")
            done = True
        elif (miles_traveled - dementors_miles_traveled) < 15 and not done:
            print("The dementors are getting close!")
            print()

        if miles_traveled >= 320 and not done:
            print("You have won!")
            done = True

        if thirst > 6 and not done:
            print("You died of thirst!")
            done = True
            print()
        elif thirst > 4 and not done:
            print("You are thirsty!")
            print()

        if hippogriff_tiredness > 8 and not done:
            print("Your hippogriff is dead!")
            done = True
            print()
        elif hippogriff_tiredness > 6 and not done:
            print("Your hippogriff is getting tired!")
            print()


main()
