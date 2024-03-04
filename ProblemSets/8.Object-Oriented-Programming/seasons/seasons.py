
from datetime import date
import operator
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    message = text_minutes(minutes(year, month, day))
    print(message)


def minutes(year, month, day):
    try:
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    timedelta = operator.sub(date.today(), birth_date)
    years_minutes = int(timedelta.total_seconds() / 60)
    return years_minutes


def text_minutes(m):
    text = p.number_to_words(m, andword="")
    return f"{text.capitalize()} minutes"
    

if __name__ == "__main__":
    main()
