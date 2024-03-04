def main():
    while True:
        fuel = input("Fraction: ")
        try:
            convert(fuel)
            break
        except ValueError:
            print("Fraction cannot be bigger than 1 and fraction must only contain numbers")
            continue
        except ZeroDivisionError:
            print("Fraction cannot be divided by 0")
            continue
    fuel_percent = convert(fuel)
    print(gauge(fuel_percent))


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    else:
        return round(int(x) / int(y) * 100)



def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
    