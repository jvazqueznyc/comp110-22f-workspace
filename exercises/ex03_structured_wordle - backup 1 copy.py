"""EX03 - Structured Wordle - 6 chances to correctly guess the 5-character secret word."""

__author__ = "730622831"

from ast import Return


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

# # emojified lines of code
# WHITE_BOX: str = "\U00002B1C"
# GREEN_BOX: str = "\U0001F7E9"
# YELLOW_BOX: str = "\U0001F7E8"
# emoji_result: str = ""

# def emojified (string_1_guess: str, string_2_secret: str) -> str:
#     """Given two strings of equal length, a emoji string is returned whose color corresponds to level of success for a letter."""
#     assert len(string_1_guess) == len(string_2_secret)
#     index_counter_of_string_1_guess = 0
#     index_counter_of_string_2_secret = 0
#     while index_counter_of_string_1_guess > len(string_2_secret):
#         if string_1_guess[index_counter_of_string_1_guess] == string_2_secret[index_counter_of_string_2_secret]:
#             emoji_result = emoji_result + GREEN_BOX
#         else:
#             if contains_char(string_2_secret, string_1_guess[index_counter_of_string_1_guess]) is True:
#                 emoji_result = emoji_result + YELLOW_BOX
#             else:
#                 emoji_result = emoji_result + WHITE_BOX                
#         index_counter_of_string_1_guess = index_counter_of_string_1_guess + 1
#         index_counter_of_string_2_secret = index_counter_of_string_2_secret + 1
#     print(emoji_result)    
    
# print(emojified("hello", "world"))

#     if secret_word_guess[index_counter_of_guess] == secret_word[index_counter_of_guess]:
#         emoji_result = emoji_result + GREEN_BOX
#     else:
#         guessed_chr_exist_elsewhere = False
#         index_counter_of_secret_word: int = 0
#         while index_counter_of_secret_word < len(secret_word):
#             if secret_word[index_counter_of_secret_word] == secret_word_guess[index_counter_of_guess]:
#                 guessed_chr_exist_elsewhere = True
#             index_counter_of_secret_word = index_counter_of_secret_word + 1
#         if guessed_chr_exist_elsewhere is True:
#             emoji_result = emoji_result + YELLOW_BOX
#         else:
#             emoji_result = emoji_result + WHITE_BOX
#     index_counter_of_guess = index_counter_of_guess + 1

# print(contains_char("dogs", "z"))


# error if single_search_chr != 1

# old cold
# secret_word: str = "codes"
# input_guess: str = input(f"Enter a 5 character word: ")
# attempt_counter: int = 0

# # ensuring secret_word_guess is the same amount of characters as secret_word
# while len(secret_word_guess) != len(secret_word):
#     secret_word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# # input is appearing on following line, however, professor wants it to appear on same line
    
# # White for letters that don’t exist. Green for letters that match at the correct position. Yellow for correct guessed letter that is in wrong position.

# # emojified function outputs boxes for each letter of guess
# WHITE_BOX: str = "\U00002B1C"
# GREEN_BOX: str = "\U0001F7E9"
# YELLOW_BOX: str = "\U0001F7E8" #contains_char function for yellow boxes

# # while loop to see if secret_word_guess has same characters as secret_word
# index_counter_of_guess: int = 0
# emoji_result: str = ""

# #main function below
# while index_counter_of_guess < len(secret_word):
#     if secret_word_guess[index_counter_of_guess] == secret_word[index_counter_of_guess]:
#         emoji_result = emoji_result + GREEN_BOX
#     else:
#         guessed_chr_exist_elsewhere = False
#         index_counter_of_secret_word: int = 0
#         while index_counter_of_secret_word < len(secret_word):
#             if secret_word[index_counter_of_secret_word] == secret_word_guess[index_counter_of_guess]:
#                 guessed_chr_exist_elsewhere = True
#             index_counter_of_secret_word = index_counter_of_secret_word + 1
#         if guessed_chr_exist_elsewhere is True:
#             emoji_result = emoji_result + YELLOW_BOX
#         else:
#             emoji_result = emoji_result + WHITE_BOX
#     index_counter_of_guess = index_counter_of_guess + 1
    

# # game is finished. print success and defeat messages
# print(emoji_result)
# if secret_word_guess == secret_word:
#     print("Woo! You got it!")
# else:
#     print("Not quite. Play again soon!")