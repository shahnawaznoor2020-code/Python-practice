import random
print("Welcome to the Game of Rolling a Dice")
while True:
    choice = input("Would you like to roll a dice (y/n)? ")
    choice = choice.lower()
    choice = choice.strip()
    if choice == "n":
        print("Thank you for playing")
        break
    elif choice == "y":
        number = random.randint(1,6)
        user_choice = int(input("Enter your choice: "))
        if number == user_choice:
            print("You got it!")
            print(f"You rolled a {number}")
        else:
            print("Wrong choice!")
            print(f"You rolled a {number}")
            print("Try again")
    else:
        print("Invalid Input")