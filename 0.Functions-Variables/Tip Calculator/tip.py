def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_dollars = d.removeprefix("$")
    return float(remove_dollars)


def percent_to_float(p):
    remove_percentage = p.removesuffix("%")
    return float(remove_percentage) / 100


main()
