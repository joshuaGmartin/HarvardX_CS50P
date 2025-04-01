def main():
    with open("alice.txt", "r") as file:
        # contents = file.read()
        # print(contents)
        contents = file.readlines()
        chapter1 = contents[11:246]

        with open("chapter1.txt", "w") as file:
            file.writelines(chapter1)
            # for line in chapter1:
            #     file.write(line)


if __name__ == "__main__":
    main()
