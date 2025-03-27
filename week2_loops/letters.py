# def main():
#     print(write_letter("Mario", "Peach"))
#     print(write_letter("Luigi", "Peach"))
#     print(write_letter("Daisy", "Peach"))
#     print(write_letter("Yoshi", "Peach"))


# def write_letter(reciever, sender):
#     sig = "\x1b[3m" + sender + "\x1b[23m"
#     return f"""
#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

#         Dear {reciever},

#         I love you.

#         Sincerely,
#         {sig}

#     +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
#     """


# main()


# =======================================


def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]

    # for i in range(len(names)):
    #     print(write_letter(names[i], "Peach"))

    for name in names:
        print(write_letter(name, "Peach"))


def write_letter(reciever, sender):
    sig = "\x1b[3m" + sender + "\x1b[23m"
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

        Dear {reciever}, 

        I love you. 

        Sincerely, 
        {sig}

    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()
