import inflect

ie = inflect.engine()

names = []

while True:
    try:
        get_name = input("Name: ").strip().title()
        names.append(get_name)
    except EOFError:
        break

print("Adieu, adieu, to " + ie.join(names))
