from pyfiglet import Figlet
import random as rnd
import sys


if len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if not sys.argv[1] == "-f" and not sys.argv[1] == "--font":
        sys.exit("Invalid usage")

f = Figlet()
font_list = f.getFonts()

if len(sys.argv) == 3:
    if sys.argv[2] not in font_list:
        sys.exit("Invalid usage")

user_input = input("Input: ")


if len(sys.argv) == 1:
    randomFont = rnd.choice(font_list)
    f.setFont(font=randomFont)
    print(f.renderText(user_input))

elif len(sys.argv) == 3:
    if "-f" == sys.argv[1] or "--font" == sys.argv[1]:
        f.setFont(font=sys.argv[2])
        print(f.renderText(user_input))
