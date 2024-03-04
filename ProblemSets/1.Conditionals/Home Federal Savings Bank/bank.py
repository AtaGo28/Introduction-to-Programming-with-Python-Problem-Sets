greeting = input("Greeting: ").strip().lower()

if greeting.lstrip("0123456789?!@#$%^&*()-_+=~`</>,.?'").startswith("hello"):
    print("$0")
elif greeting.lstrip("0123456789?!@#$%^&*()-_+=~`</>,.?'").startswith("h"):
    print("$20")
else:
    print("$100")
