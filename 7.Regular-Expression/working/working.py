import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(\d{1,2}):?([0-5][0-9])? (AM|PM) to (\d{1,2}):?([0-5][0-9])? (AM|PM)$", s
    ):
        hour1 = int(matches.group(1))
        if matches.group(3) == "PM" and hour1 != 12:
            hour1 += 12
        elif matches.group(3) == "AM" and hour1 == 12:
            hour1 -= 12
        if matches.group(2):
            time1 = f"{hour1:02}:{matches.group(2)}"
        else:
            time1 = f"{hour1:02}:00"

        hour2 = int(matches.group(4))
        if matches.group(6) == "PM" and hour2 != 12:
            hour2 += 12
        elif matches.group(6) == "AM" and hour2 == 12:
            hour2 -= 12
        if matches.group(5):
            time2 = f"{hour2:02}:{matches.group(5)}"
        else:
            time2 = f"{hour2:02}:00"

        return f"{time1} to {time2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
