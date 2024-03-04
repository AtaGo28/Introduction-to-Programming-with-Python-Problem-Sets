def main():
    user_input = input("Input: ")
    print("Output:", shorten(user_input))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    for chr in word:
        if chr.lower() in vowels:
            output += chr.replace(chr, "")
        else:
            output += chr
    return output


if __name__ == "__main__":
    main()


