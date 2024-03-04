import random as rnd


def main():
    lvl = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        answer = None

        for _ in range(3):
            try:
                answer = input(f"{x} + {y} = ")
                if int(answer) == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Your score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            continue


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    elif level == 1:
        return rnd.randint(0, 9)
    else:
        return rnd.randint(10 ** (level - 1), 10**level - 1)


if __name__ == "__main__":
    main()
