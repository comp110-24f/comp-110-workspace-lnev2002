"""Program calculates tea bags, treats, and cost given number of people."""

__author__: str = "730482901"


def main_planner(guests: int) -> None:
    """Function prints out information about tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# lines 8-10 str and int cannot be added, need to convert tea_bags and treats to str
# cost calculates tea_count given # of tea bags, tea_count in terms of fxn tea_bags
# remember to put spaces in strings


def tea_bags(people: int) -> int:
    """Function calculates amount of tea bags needed given a number of people."""
    return people * 2


def treats(people: int) -> int:
    """Function calculates amount of treats need given a number of people."""
    return int((tea_bags(people=people)) * 1.5)


# tea_bags * 1.5 gives type float, needs to be converted to int to match return type
# keyword argument is people=people
# int must be outside of tea_bags, not inside


def cost(tea_count: int, treat_count: int) -> float:
    """Function calculates cost of treats and bags given a number of people."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
