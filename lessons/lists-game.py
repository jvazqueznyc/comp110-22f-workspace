"""Examples of using lists in a simple 'game'."""

# randint is a function from the random. randint generates random interger
from random import randint


rolls: list[int] = list() # creating an list of intergers that is empty

# while the list is empty or the last roll does not equal int 1, keep rolling
while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))
print(rolls)

rolls.pop(len(rolls) - 1)
print(rolls)

# summing the values of all rolls
i: int = 0
sum: int = 0
# we already removed 1 in the final index so we don't need to do rolls[len(rolls) - 1]
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")
