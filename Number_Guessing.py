import random

def number_guessing_game():
    number_to_guess=random.randint(1,25)
    attempts=0

    print("Welcome to the Number Guessing Game")
    print("Guess a number between 1-25:")

    while True:
        try:
            guess=int(input("Enter the Guess:"))
            attempts+=1

            if guess<number_to_guess:
                print("Too low! Try again")

            elif guess>number_to_guess:
                print("Too high! Try again")

            else:
                print("Correct!!")
                break
        except ValueError:
            print("Please Enter a valid number")


number_guessing_game()
