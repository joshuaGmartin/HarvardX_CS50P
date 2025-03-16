name = input("Name?: ")

# if name == "Harry":
#     print("Gryffinfor")
# elif name == "Hermione":
#     print("Gryffinfor")
# elif name == "Ron":
#     print("Gryffinfor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffinfor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# like switch in JS
# match name:
#     case "Harry":
#         print("Gryffinfor")
#     case "Hermione":
#         print("Gryffinfor")
#     case "Ron":
#         print("Gryffinfor")
#     case "Draco":
#         print("Slytherin")
#     # python catch all
#     case _:
#         print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffinfor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
