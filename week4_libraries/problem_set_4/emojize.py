import emoji


def main():
    msg = ":1st_place_medal:"
    print(emoji.emojize("Output:" + msg, language="alias"))
    msg = ":money_bag:"
    print(emoji.emojize("Output:" + msg, language="alias"))
    msg = ":smile_cat:"
    print(emoji.emojize("Output:" + msg, language="alias"))
    msg = input("Input: ")
    print(emoji.emojize("Output: " + msg, language="alias"))


main()
