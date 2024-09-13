"""Challenge Question 00 on Functions"""

__author__ = "730482901"


def mimic(message: str) -> str:
    """The function repeats back its input as output."""
    return message


def main() -> None:
    """This is the main function that unites different functions."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
