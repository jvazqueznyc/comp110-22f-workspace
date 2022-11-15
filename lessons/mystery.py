def mystery (n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
            i += 1
        return "ahh"