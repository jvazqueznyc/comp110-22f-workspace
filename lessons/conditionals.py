"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day.")
else:
    print("Sorry, you guessed incorrectly.")
    if guess > SECRET:
        print("Sorry. You guessed too high.")
        print("Try running the program again.")
    else:
        print("Sorry. You guessed too low.")
        print("Try running the program again.")

print("Game over.")

print(guess + SECRET)