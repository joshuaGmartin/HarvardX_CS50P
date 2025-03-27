# def main():
#     counts = {}
#     words = get_words("address.txt")
#     lowercase_words = [word.lower() for word in words]
#     filtered_words = [word for word in lowercase_words if len(word) > 4]

#     # print(words)

#     for word in filtered_words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     print(counts)


# def get_words(filename):
#     with open(filename, "r") as file:
#         content = file.read()
#     return content.split(" ")


# main()

# ================================


def main():
    words = get_words("address.txt")
    lowercase_filtered_words = [word.lower() for word in words if len(word) > 4]

    counts = {
        word: lowercase_filtered_words.count(word) for word in lowercase_filtered_words
    }

    print(counts)


def get_words(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content.split(" ")


main()
