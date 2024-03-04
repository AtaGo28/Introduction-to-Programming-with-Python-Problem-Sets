while True:
    fuel = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        fuel_percent = round(int(x) / int(y) * 100)
        if int(x) > int(y):
            continue
        break
    except (ValueError, ZeroDivisionError):
        pass


if 0 <= int(fuel_percent) <= 1:
    print("E")
elif 100 >= int(fuel_percent) >= 99:
    print("F")
else:
    print(int(fuel_percent), "%", sep="")
