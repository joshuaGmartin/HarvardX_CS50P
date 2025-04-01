from PIL import Image
from PIL import ImageOps
import sys

required_file_formats = ["png", "jpeg", "jpg"]
print(sys.argv[2].split(".")[1])


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] not in required_file_formats:
        sys.exit("Invalid input")
    elif sys.argv[2].split(".")[1] not in required_file_formats:
        sys.exit("Invalid output")
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open("shirt.png") as shirt, Image.open(sys.argv[1]) as person:
            person = ImageOps.fit(person, shirt.size)
            person.paste(shirt, (0, 0), shirt)

            person.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


main()
