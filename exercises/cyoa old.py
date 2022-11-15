"""EX06 - Choose Your Own Adventure - A fun guessing game."""

__author__ = "730622831"

# Imported stuff
import random

# Global variable declarations below.
points: int = 50
player: str = input("To begin, what is your name?: ")

"""Emoji collection below."""
INSULTING_SHRUG: str = "\U0001F937"
SKULL_OF_DEFEAT: str = "\U00002620"
CELEBRATION: str = "\U0001F389"
WISE_WIZARD: str = "\U0001F9D9"
DEVIL: str = "\U0001F608"
def main() -> None:
  """Entry point of program."""

  greet()

  """Following code asks user to choose between 3 initial options before entering initial_game_choices function"""
  print("1) Guess a number.      2) Guess a letter.      3) Exit game.")
  igc_input = int(input("Choose an option between 1 and 3 to continue: "))
  initial_game_choices(igc_input)

  return None


def greet() -> None:
  """The greet function prints a welcome message to give some context to game and asks the player for their name."""
  print(str("Hello! This is a fun guessing game."))
  return


def initial_game_choices(igc_chosen_number: int) -> None:
  """The initial_game_choices function asks user to choose between 3 initial options."""
  global points
  if igc_chosen_number < 1:
    igc_chosen_number = int(input("Choose an option between 1 and 3 to continue: "))
  if igc_chosen_number > 3:
    igc_chosen_number = int(input("Choose an option between 1 and 3 to continue: "))
  if igc_chosen_number == 1:
    first_igc_numbers()
  if igc_chosen_number == 2:
    points = second_igc_letters(points) #CHECK TO SEE THAT POINTS IS UPDATED
  if igc_chosen_number == 3:
    print(f"Guess you couldn't handle it. {INSULTING_SHRUG} Goodbye.")
  return None


"""First game option function that player chooses in the initial_game_choices function."""
def first_igc_numbers() -> None:
  global points
  print(f"{player}, you have {points} points!")
  print(f"You only have 6 attempts to guess the right number.\nYou can have up to 100 points. If you get to 0 points, you lose.\nYour points will increase by 10 every time your guess is closer to the correct number.\nYour points will decrease by 10 every time your guess is farther away from the correct number.\nIf your last two guesses are the same distance from the correct number, your points won't change.\nReady? Guess wisely. {WISE_WIZARD}\n")
  points
  correct_number = random.randint(0, 250)
  number_guess: int = 0
  guess_number_list: list[int] = []
  i: int = 0 # Attempt counter variable.
  while points > 0 and i < 6:
    number_guess = int(input(f"Guess a number between 0 and 250: "))
    guess_number_list.append(number_guess)
    
    """Correct guess winning situation."""
    if correct_number == number_guess:
      print(f"Congratulations, {player}! {CELEBRATION} You win!\nBet you can't do it twice in a row. Hahaha {DEVIL}")
      points += 10
      i += 1
      # Game ending stats.
      print(f"Your point total was {points} over {i}/6 attempts.\n") # Reports point and attempt totals after initial_game_choices function completes.
      return

    """Hints to guide player after guess."""
    if i < 5:
      if correct_number > number_guess:
        print("Try a larger number.")
      if correct_number < number_guess:
        print("Try a smaller number.")

    """Adding or subtracting points based on improved or worsened proximity to correct number."""
    if i == 0:
        # ^ Do this because on the first try there won't be a penultimate guess.
        i += 1
        points += 0
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
          elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
              # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
              points += 0
          else:
              # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
              points -= 10
          print(f"Your point total is {points} over {i}/6 attempts.\n")
      if i == 5:   
          # Last try (sixth attempt) situation
          if abs_diff_correct_and_latest_guess < abs_diff_correct_and_penultimate_guess:
              # ^ If absolute difference between correct and latest guess is less than that of correct and penultimate guess, add points.
              points += 10
          elif abs_diff_correct_and_latest_guess == abs_diff_correct_and_penultimate_guess:
              # ^ If absolute difference between the correct and latest guess and that of the correct and penultimate guess are equal, don't change points value.
              points += 0
          else:
              # ^ If absolute difference between correct and latest guess is larger than that of correct and penultimate guess, subtract points.
              points -= 10
    if points == 0 or i == 6:
        # Lost situation.
        print(f"You lose! {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}  {SKULL_OF_DEFEAT}\nThe correct answer was {correct_number}.\nHope you can find an easier game. Hahahahahaha!")
        # Game ending stats.
        print(f"Your point total was {points} over {i}/6 attempts.\n") # Reports point and attempt totals after initial_game_choices function completes.


"""Second game option function that player chooses in the initial_game_choices function. Hahahahaha!"""
def second_igc_letters(second_igc_parameter_points: int) -> int:
  # Points should be a local variable in this function.
  second_igc_parameter_points = points
  points = 50
  correct_number = random.rand()
  print(f"{player}, you have {points} points!")
  print(f"You only have 3 attempts to guess the right letter.\nYou can have up to 100 points. If you get to 0 points, you lose.\nYour points will increase by 25 every time your guess is closer to the correct number.\nYour points will decrease by 25 every time your guess is farther away from the correct number.\nIf your last two guesses are the same distance from the correct number, your points won't change.\nReady? Guess wisely. {WISE_WIZARD}\n")
  correct_number = random.randint(0, 250)
  #this function should return the player’s total points after any interactions it leads to
  return second_igc_parameter_points


if __name__ == "__main__":
  main()

#this marks trying to change to 6 attempts