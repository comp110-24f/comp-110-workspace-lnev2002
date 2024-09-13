"""practice with conditionals"""


def less_than_10(num: int) -> bool:
    """tell me if num 10 < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("Big number")
    print("Have a nice day")


less_than_10(num=5)


def should_i_eat(hungry: bool) -> None:
    if hungry:
        print("Eat some food")
    else:
        print("do comp 110 homework instead")
    print("I'm proud of you")


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """check if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    if weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
