months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").strip().title()

    if "," in date:
        date = date.replace(",", "")
        month, day, year = date.split()
        if month in months:
            month = months.index(month) + 1
    elif "/" in date:
        month, day, year = date.split("/")
    else:
        continue

    try:
        if 0 < int(month) <= 12 and 0 < int(day) <= 31 and int(year) != 0:
            break
    except ValueError:
        pass

print(year, f"{int(month):02}", f"{int(day):02}", sep="-")
