def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

def love_two(subject: str, n: int) -> str:
    """Given a subject to receive statement and a number of times for statement to repeat, repeat love statement n amount of times."""
    love_msg: str = f"I love you, {subject}."
    i: int = 0
    while i < n:
        i += 1
    return love_msg