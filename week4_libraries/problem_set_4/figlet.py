import random
import pyfiglet
import sys

fonts = pyfiglet.FigletFont.getFonts()


def main():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("wrong number of args")
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            sys.exit("invalid use")
        if sys.argv[2] not in fonts:
            sys.exit("not a font")

    text = input("Input: ")

    if len(sys.argv) == 1:
        font_choice = random.choice(fonts)

        print(pyfiglet.figlet_format(text, font=font_choice))

    else:
        print(pyfiglet.figlet_format(text, font=sys.argv[2]))


main()
