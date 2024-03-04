def main():
    expression = input("Expression: ").strip()
    print(calculate(expression))


def calculate(n):
    x, y, z = n.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)
    else:
        return None


main()
