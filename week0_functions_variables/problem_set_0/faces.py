def main():
    phrase = "Hello :)"
    print(convert(phrase))
    phrase = "Goodbye :("
    print(convert(phrase))
    phrase = "Hello :) Goodbye :("
    print(convert(phrase))


def convert(phrase):
    converted_words = []

    for word in phrase.split():
        if word == ":)":
            converted_words.append("🙂")
        elif word == ":(":
            converted_words.append("🙁")
        else:
            converted_words.append(word)

    return " ".join(converted_words)


main()

# simpler method
# phrase = "Hello :)"
# print(phrase.replace(":)", "🙂").replace(":(", "🙁"))
# phrase = "Goodbye :("
# print(phrase.replace(":)", "🙂").replace(":(", "🙁"))
# phrase = "Hello :) Goodbye :("
# print(phrase.replace(":)", "🙂").replace(":(", "🙁"))
