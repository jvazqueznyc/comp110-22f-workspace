"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730622831"


five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character_of_word: str = input("Enter a single character: ")

if len(single_character_of_word) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character_of_word + " in " + five_character_word)

matching_characters_of_word: int = 0


if single_character_of_word == five_character_word[0]:
    print(single_character_of_word + " found at index 0")
    matching_characters_of_word = matching_characters_of_word + 1 

if single_character_of_word == five_character_word[1]:
    print(single_character_of_word + " found at index 1")
    matching_characters_of_word = matching_characters_of_word + 1

if single_character_of_word == five_character_word[2]:
    print(single_character_of_word + " found at index 2")
    matching_characters_of_word = matching_characters_of_word + 1

if single_character_of_word == five_character_word[3]:
    print(single_character_of_word + " found at index 3")
    matching_characters_of_word = matching_characters_of_word + 1

if single_character_of_word == five_character_word[4]:
    print(single_character_of_word + " found at index 4")
    matching_characters_of_word = matching_characters_of_word + 1


if matching_characters_of_word == 1:
    print(str(matching_characters_of_word) + " instance of " + single_character_of_word + " found in " + five_character_word)

if matching_characters_of_word > 1:
    print(str(matching_characters_of_word) + " instances of " + single_character_of_word + " found in " + five_character_word)

if matching_characters_of_word == 0:
    print("No instances of " + single_character_of_word + " found in " + five_character_word)