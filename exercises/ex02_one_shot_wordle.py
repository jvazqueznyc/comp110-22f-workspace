"""EX02 - One Shot Worldle game - One chance to correctly guess the secret word."""

__author__ = "730622831"

secret_word: str = "python"
secret_word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
attempt_counter: int = 0

# ensuring secret_word_guess is the same amount of characters as secret_word
while len(secret_word_guess) != len(secret_word):
    secret_word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# input is appearing on following line, however, professor wants it to appear on same line
    

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# while loop to see if secret_word_guess has same characters as secret_word
index_counter_of_guess: int = 0
emoji_result: str = ""

while index_counter_of_guess < len(secret_word):
    if secret_word_guess[index_counter_of_guess] == secret_word[index_counter_of_guess]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        guessed_chr_exist_elsewhere = False
        index_counter_of_secret_word: int = 0
        while index_counter_of_secret_word < len(secret_word):
            if secret_word[index_counter_of_secret_word] == secret_word_guess[index_counter_of_guess]:
                guessed_chr_exist_elsewhere = True
            index_counter_of_secret_word = index_counter_of_secret_word + 1
        if guessed_chr_exist_elsewhere is True:
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX
    index_counter_of_guess = index_counter_of_guess + 1
    

# game is finished. print success and defeat messages
print(emoji_result)
if secret_word_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")