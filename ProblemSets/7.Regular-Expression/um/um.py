import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    num = 0
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        for _ in matches:
            num += 1
    return num


if __name__ == "__main__":
    main()
