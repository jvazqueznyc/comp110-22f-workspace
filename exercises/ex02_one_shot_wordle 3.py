"""EX02 - One Shot Worldle game - One chance to correctly guess the secret word."""

__author__ = "730622831"

secret_word: str = "python"
secret_word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
attempt_counter: int = 0


while len(secret_word_guess) != len(secret_word):
    secret_word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
    #input is appearing on following line, however, professor wants it to appear on same line
    


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


index_counter_of_guess: int = 0
emoji_result: str = ""

while index_counter_of_guess < len(secret_word):
    index_counter_of_guess = index_counter_of_guess + 1
    if secret_word_guess[index_counter_of_guess] == secret_word[index_counter_of_guess]:
        emoji_result = emoji_result + GREEN_BOX
    else:
        guessed_chr_exist_elsewhere = False
        index_counter_of_secret_word: int = 0
        while guessed_chr_exist_elsewhere == False and index_counter_of_secret_word < len(secret_word):
            if secret_word[index_counter_of_secret_word] == secret_word_guess[index_counter_of_secret_word]:
                guessed_chr_exist_elsewhere = True
                emoji_result = emoji_result + WHITE_BOX
            if secret_word[index_counter_of_secret_word] != secret_word_guess[index_counter_of_secret_word]:
                emoji_result = emoji_result + YELLOW_BOX
        index_counter_of_secret_word = index_counter_of_secret_word + 1
    

print(emoji_result)
if secret_word_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")