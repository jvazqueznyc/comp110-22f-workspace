"""EX03 - Structured Wordle - 6 chances to correctly guess the 5-character secret word."""

__author__ = "730622831"

#
def contains_char (string_of_multiple_chrs: str, single_search_chr: str) -> bool:
    """contains_char checks to see if single character is found anywhere in string of characters"""
    assert len(single_search_chr) == 1
    index_counter_of_string: int = 0
    found_searched_character = False
    while index_counter_of_string < len(string_of_multiple_chrs):
        if single_search_chr == string_of_multiple_chrs[index_counter_of_string]:
            found_searched_character = True
            return found_searched_character
        else:
            found_searched_character = False
        index_counter_of_string = index_counter_of_string + 1
    return found_searched_character


def emojified (string_1_guess: str, string_2_secret: str) -> str:
    """Given two strings of equal length, a emoji string is returned whose color corresponds to level of success for a letter."""
    assert len(string_1_guess) == len(string_2_secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result: str = ""
    index_counter_of_string_1_guess = 0
    index_counter_of_string_2_secret = 0
    while index_counter_of_string_1_guess < len(string_2_secret):
        if string_1_guess[index_counter_of_string_1_guess] == string_2_secret[index_counter_of_string_2_secret]:
            emoji_result = emoji_result + GREEN_BOX
        else:
            if contains_char(string_2_secret, string_1_guess[index_counter_of_string_1_guess]) is True:
                emoji_result = emoji_result + YELLOW_BOX
            else:
                emoji_result = emoji_result + WHITE_BOX                
        index_counter_of_string_1_guess = index_counter_of_string_1_guess + 1
        index_counter_of_string_2_secret = index_counter_of_string_2_secret + 1
    print(emoji_result)


def input_guess (expected_length_of_guess: int) -> str:
    """Requests a required length of guess, asks user for a guess that is equal to that length, and finally returns guess to caller"""
    secret_word_guess: str = input(f"Enter a {str(expected_length_of_guess)}-letter word: ")
    while len(secret_word_guess) != expected_length_of_guess:
        secret_word_guess = input(f"That wasn't {str(expected_length_of_guess)} chars! Try again: ")
    else:
        return secret_word_guess

#
def main() -> None:
    """The entrypoint of the program and main game loop."""
    correct_secret_word: str = "codescodes"
    completed_attempts: int = 0
    won_game: bool = False
    while completed_attempts < 6 and won_game == False:
        print(f"=== Turn {completed_attempts + 1}/6 ===")
        input_guess_return = input_guess((len(correct_secret_word)))
        emojified(input_guess_return, correct_secret_word)
        if input_guess_return == correct_secret_word:
            print(f"You won in {(completed_attempts + 1)}/6 turns!")
            won_game = True
            return
        completed_attempts = completed_attempts + 1
    if completed_attempts == 6:
        print("X/6 - Sorry, try again tomorrow!")
        return

if __name__ == "__main__":
    main()