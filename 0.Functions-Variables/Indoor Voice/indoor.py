def main():
    start()
    print("Thank you!...")


def start(intro="Whould you like to say anything?... "):
    print(intro)
    text = input("Start typing... ").casefold()
    print(text)


main()
