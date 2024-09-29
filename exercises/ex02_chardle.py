"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730482901"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """user inputs word and function returns error if word is not 5 characters"""
    user_word = str(input("Enter a 5-character word:"))
    if len(user_word) > 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return user_word
    elif len(user_word) < 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return user_word
    else:
        return user_word


# if, elif, else can be used because there are 3 options
# can define local variable without following name: type = value format


def input_letter() -> str:
    """user inputs single character and function returns error if word is not single."""
    single_character = str(input("Enter a single character:"))
    if len(single_character) > 1:
        print("Error: Character must be a single character.")
        exit()
        return single_character
    elif len(single_character) < 1:
        print("Error: Character must be a single character.")
        exit()
        return single_character
    else:
        return single_character


# need to account for if people put no character


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count_char: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count_char = count_char + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count_char = count_char + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count_char = count_char + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count_char = count_char + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count_char = count_char + 1
    if count_char == 0:
        print("No instances of " + letter + " in " + word)
    elif count_char == 1:
        print(str(count_char) + " instance of " + letter + " in " + word)
    else:
        print(str(count_char) + " instances of " + letter + " in " + word)


# Have to account for 1 instance differently than > 1 instances

if __name__ == "__main__":
    main()
