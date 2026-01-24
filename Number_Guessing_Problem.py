import random
print("Welcome to the Number Guessing Game. We have a number that needs to be guessed. We have to guessed. You have 10 chances.")
print("The number is between 1 and 100.")
count=10
guess=random.randint(1,100)
while count>0:
    print("You have",count,"chances to guess the number.")
    user_choice=int(input("Guess the number: "))
    if user_choice==guess:
        print("Congrats! You guessed the number!")
        count=count-1
        break
    elif user_choice>guess:
        print("Your is choice Wrong! Try lower")
        count=count-1
    else:
        print("Your is choice Wrong! Try higher")
        count=count-1
if count==0:
    print("Bad Luck. Attempts Over! try again next time")
print("Thank you for playing")
print(f"The number was {guess} .Game over!!!")