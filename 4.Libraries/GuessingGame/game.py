import random as rnd

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    if n > 0:
        break

i = rnd.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < 0:
        continue
    elif guess > i:
        print("Too Large!")
        continue
    elif guess < i:
        print("Too Small!")
        continue
    else:
        print("Just Right!")
        break
