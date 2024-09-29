"""Code allows user to guess a number and tells user if it is correct, high, or low."""

__author__: str = "730482901"


def guess_a_number() -> None:
    secret: int = 7
    number = int(input("Guess a number:"))
    print(("Your guess was ") + str(number))
    if number == 7:
        print("You got it!")
    else:
        if number < 7:
            print(("Your guess was too low! The secret number is ") + str(secret))
        else:
            print(("Your guess was too high! The secret number is ") + str(secret))


if __name__ == "__main__":
    guess_a_number()
