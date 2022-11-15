"""EX06 - Choose Your Own Adventure - A fun guessing game."""

__author__ = "730622831"


# Imported stuff
import random


"""Emoji collection below."""
INSULTING_SHRUG: str = "\U0001F937"
SKULL_OF_DEFEAT: str = "\U00002620"
CELEBRATION: str = "\U0001F389"
WISE_WIZARD: str = "\U0001F9D9"
DEVIL: str = "\U0001F608"


# Global variable declarations below.
points: int = 50
player: str = ""


def main() -> None:
    """Entry point of program."""
    global points
    
    greet()

    """Initial Game Choices AKA Game Loop: Asks user to choose between three game options."""
    playing = True
    while playing is True:
        print(f"{player}, you have {points} points!")
        print("\nGame menu:\n")
        print("1) Guess a number.      2) Guess a letter.      3) Exit game.")
        igc_chosen_number = int(input("Choose an option between 1 and 3 to continue: "))
        while (igc_chosen_number != 1) and (igc_chosen_number != 2) and (igc_chosen_number != 3):
            igc_chosen_number = int(input("Input must be 1, 2, or 3. Choose an option between 1 and 3 to continue: "))
        if igc_chosen_number < 1:
            igc_chosen_number = int(input("Choose an option between 1 and 3 to continue: "))
        if igc_chosen_number > 3:
            igc_chosen_number = int(input("Choose an option between 1 and 3 to continue: "))
        if igc_chosen_number == 1:
            first_igc_numbers()
        if igc_chosen_number == 2:
            points = second_igc_letters(points)  # CHECK TO SEE THAT POINTS IS UPDATED.
        if igc_chosen_number == 3:
            print(f"Guess you couldn't handle it. {INSULTING_SHRUG} Goodbye.")
            print(f"Your point total was {points}.")
            playing = False


def greet() -> None:
    """The greet function prints a welcome message to give some context to game and asks the player for their name."""
    global player
    print(str("\nHello! This is a fun guessing game."))
    player = input("To begin, what is your name?: ")
    return


def first_igc_numbers() -> None:
    """First game option function that player chooses in the initial_game_choices function."""  
    global points
    print(f"{player}, you have {points} points!")
    print(f"You only have 6 attempts to guess the right number.\nYou can have up to 100 points. If you get to 0 points, you lose.\nYour points will increase by 10 every time your guess is closer to the correct number.\nYour points will decrease by 10 every time your guess is farther away from the correct number.\nIf your last two guesses are the same distance from the correct number, your points won't change.\nReady, {player}? Guess wisely. {WISE_WIZARD}\n")
    points
    correct_number = random.randint(0, 250)
    number_guess: int = 0
    guess_number_list: list[int] = []
    i: int = 0  # Attempt counter variable.
    while points > 0 and i < 6:
        number_guess = int(input("Guess a number between 0 and 250: "))
        guess_number_list.append(number_guess)
        
        """Correct guess winning situation."""
        if correct_number == number_guess:
            print(f"Congratulations, {player}! {CELEBRATION} You win!\nBet you can't do it twice in a row. Hahaha {DEVIL}")
            points += 10
            if points > 100:
                points = 100 
            i += 1
            # Game ending stats.
            print(f"Your point total was {points} over {i}/6 attempts.\n")  # Reports point and attempt totals after initial_game_choices function completes.
            return

        """Hints to guide player after guess."""
        if i < 5:
            if correct_number > number_guess:
                print(f"Try a larger number, {player}.")
            if correct_number < number_guess:
                print(f"Try a smaller number, {player}.")

        """Adding or subtracting points based on improved or worsened proximity to correct number."""
        if i == 0:
            # ^ Do this because on the first try there won't be a penultimate guess.
            i += 1
            points += 0
            if points > 100:
                points = 100 
            print(f"Your point total is {points} over {i}/6 attempts.\n")    
        elif i >= 1:
            # ^ There will now be two elements in guess list so we can now compare their distances to the correct number.
            abs_diff_correct_and_latest_guess: int = abs(correct_number - number_guess)
            abs_diff_correct_and_penultimate_guess: int = abs(correct_number - guess_number_list[len(guess_number_list) - 2])
            i += 1
            if i < 6:
                if abs_diff_correct_and_latest_guess < abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between correct and latest guess is less than that of correct and penultimate guess, add points.
                    points += 10
                    if points > 100:
                        points = 100 
                elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
                    points += 0
                    if points > 100:
                        points = 100 
                else:
                    # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
                    points -= 10
                print(f"Your point total is {points} over {i}/6 attempts.\n")
            if i == 5:   
                # Last try (sixth attempt) situation
                if abs_diff_correct_and_latest_guess < abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between correct and latest guess is less than that of correct and penultimate guess, add points.
                    points += 10
                    if points > 100:
                        points = 100 
                elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
                    points += 0
                    if points > 100:
                        points = 100 
                else:
                    # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
                    points -= 10
        if points == 0 or i == 6:
            # Lost situation.
            print(f"You lose! {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}\nThe correct answer was {correct_number}.\nHope you can find an easier game. Hahahahahaha!")
            # Game ending stats.
            print(f"Your point total was {points} over {i}/6 attempts.\n")  # Reports point and attempt totals after initial_game_choices function completes.


def second_igc_letters(second_igc_parameter_points: int) -> int:
    """Second game option function that player chooses in the initial_game_choices function. Hahahahaha!"""
    # Points should be a local variable in this function.
    points: int = 0
    points = second_igc_parameter_points
    alphabet_list: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    correct_letter = random.choice(alphabet_list)
    letter_guess: str = ""
    guess_letter_list: list[str] = []
    i2: int = 0  # Attempt counter variable.
    print(f"{player}, you have {points} points!")
    print(f"You only have 3 attempts to guess the right letter.\nYou can have up to 100 points. If you get to 0 points, you lose.\nYour points will increase by 25 every time your guess is closer to the correct number.\nYour points will decrease by 25 every time your guess is farther away from the correct number.\nIf your last two guesses are the same distance from the correct number, your points won't change.\nReady, {player}? Guess wisely. {WISE_WIZARD}\n")
    while points > 0 and i2 <= 3:
        letter_guess = input("Guess a capital letter between A and Z: ")
        while (letter_guess != "A") and (letter_guess != "B") and (letter_guess != "C") and (letter_guess != "D") and (letter_guess != "E") and (letter_guess != "F") and (letter_guess != "G") and (letter_guess != "H") and (letter_guess != "I") and (letter_guess != "J") and (letter_guess != "K") and (letter_guess != "L") and (letter_guess != "M") and (letter_guess != "N") and (letter_guess != "O") and (letter_guess != "P") and (letter_guess != "Q") and (letter_guess != "R") and (letter_guess != "S") and (letter_guess != "T") and (letter_guess != "U") and (letter_guess != "V") and (letter_guess != "W") and (letter_guess != "X") and (letter_guess != "Y") and (letter_guess != "Z"):
            letter_guess = input("Input must be a capital letter between A and Z. Try again: ")
        guess_letter_list.append(letter_guess)
        """Correct guess winning situation."""
        if correct_letter == letter_guess:
            print(f"Congratulations, {player}! {CELEBRATION} You win!\nBet you can't do it twice in a row. Hahaha {DEVIL}")
            points += 25
            if points > 100:
                points = 100  
            i2 += 1
            # Game ending stats.
            print(f"Your point total was {points} over {i2}/3 attempts.\n")
            return
        """Hints to guide player after guess."""
        if i2 < 2:
            if correct_letter > letter_guess:
                print(f"Try a letter closer to the end of the alphabet, {player}.")
            if correct_letter < letter_guess:
                print(f"Try a letter closer to the beginning of the alphabet, {player}.")
        """Adding or subtracting points based on improved or worsened proximity to correct number."""
        if i2 == 0:
            # ^ Do this because on the first try there won't be a penultimate guess.
            points += 0
            if points > 100:
                points = 100 
            i2 += 1
            print(f"Your point total is {points} over {i2}/3 attempts.\n")      
        elif i2 == 1:
            # ^ There will now be two elements in guess list so we can now compare their distances to the correct number.
            abs_diff_correct_and_latest_guess: int = abs(ord(correct_letter) - ord(letter_guess))
            abs_diff_correct_and_penultimate_guess: int = abs(ord(correct_letter) - ord(guess_letter_list[len(guess_letter_list) - 2]))
            if i2 == 1:
                if abs_diff_correct_and_latest_guess < abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between correct and latest guess is less than that of correct and penultimate guess, add points.
                    points += 25
                    if points > 100:
                        points = 100
                elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
                    points += 0
                    if points > 100:
                        points = 100 
                elif abs_diff_correct_and_latest_guess > abs_diff_correct_and_penultimate_guess:
                    # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
                    points -= 25
                i2 += 1
                print(f"Your point total is {points} over {i2}/3 attempts.\n")
        elif i2 == 2:   
            # Last try (third attempt) situation
            if abs_diff_correct_and_latest_guess < abs_diff_correct_and_penultimate_guess:
                # ^ If absolute difference between correct and latest guess is less than that of correct and penultimate guess, add points.
                points += 25
                if points > 100:
                    points = 100 
            elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
                # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
                points += 0
                if points > 100:
                    points = 100
            if abs_diff_correct_and_latest_guess > abs_diff_correct_and_penultimate_guess:
                # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
                points -= 25
            i2 += 1
        """Losing situation below."""  
        if points == 0 or i2 == 3:
            print(f"You lose! {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}\nThe correct answer was {correct_letter}.\nHope you can find an easier game. Hahahahahaha!")
            # Game ending stats.
            print(f"Your point total was {points} over {i2}/3 attempts.\n")  # Reports point and attempt totals after initial_game_choices function completes.
            i2 += 1
    # Next, return local points variable value to update the global points variable value.
    return points


if __name__ == "__main__":
    main()