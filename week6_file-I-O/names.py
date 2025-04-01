# names = []

# for _ in range(3):
#     # name = input("Name?: ")
#     # names.append(name)
#     names.append(input("Name?: "))

# for name in sorted(names):
#     print(f"hello, {name}")


# ===============================


# name = input("Name: ")


# # file = open("names.txt", "w")  # "w" overwrites file (recreating)
# file = open("names.txt", "a")  # "a" appends, but no new line (like concat)
# # file.write(name)
# # file.write("\n")
# file.write(f"{name}\n")
# file.close()


# ===============================

# name = input("Name: ")

# # auto closes
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# ===============================

#  with open("names.txt", "r") as file:
#     lines = file.readlines()  # returns list

# for line in lines:
#     print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# ===============================

# names = []

# with open("names.txt") as file:  # default is "r"
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print("hello,", name)

# ===============================

with open("names.txt") as file:
    for line in sorted(file):  # readlines() allow for lines[i]
        print("hello", line.rstrip())
