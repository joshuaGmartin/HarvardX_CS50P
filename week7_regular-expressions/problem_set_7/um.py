import re


def main():
    text = "um"
    # text = "um?"
    # text = "Um, thanks for the album."
    # text = "Um, thanks, um..."
    # text = "hello"
    # text = "yummy"
    print(count(text))


def count(text):
    matches = re.findall(r"\bum\b", text, re.IGNORECASE)

    return len(matches)


if __name__ == "__main__":
    main()
