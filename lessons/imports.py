"""Examples of importing in Pyhon"""

# from the module lessons import the module of helpers
from lessons import helpers


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))


if __name__ == "__main__":
    main()