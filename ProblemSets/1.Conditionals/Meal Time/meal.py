def main():
    time = input("What time is it? ")
    meal_time = convert(time)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")


def convert(time):
    if "a.m." in time or "p.m." in time:
        clock, am_pm = time.split(" ")
        hours, minutes = clock.split(":")
        if "p.m." in am_pm and int(hours) != 12:
            hours = int(hours) + 12
    else:
        hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours


if __name__ == "__main__":
    main()
