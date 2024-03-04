def main():
    greeting = input("Greeting: ").strip()
    print(f"$", value(greeting), sep="")

def value(greeting):
    if greeting.lstrip("0123456789?!@#$%^&*()-_+=~`</>,.?'").lower().startswith("hello"):
        return 0
    elif greeting.lstrip("0123456789?!@#$%^&*()-_+=~`</>,.?'").lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
