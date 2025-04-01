# with open("students.csv") as file:
#     # for line in file:
#     #     row = line.rstrip().split(",")
#     #     print(f"{row[0]} is in {row[1]}")
#     for line in file:
#         name, house = line.rstrip().split(",")  # More Pythonic
#         print(f"{name} is in {house}")

# ==========================================

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

# ==========================================

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         student = {"house": house, "name": name}
#         students.append(student)


# def get_name(student):
#     return student["name"]


# def get_house(student):
#     return student["house"]


# # for student in sorted(students, key=get_house, reverse=True):
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# ==========================================

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"house": house, "name": name}
#         students.append(student)


# # lambda function (anon func)
# for student in sorted(students, key=lambda x: x["name"]):
#     print(f"{student['name']} is in {student['house']}")

# ==========================================


# import csv

# students = []

# # with open("students.csv") as file:
# #     reader = csv.reader(file)
# #     # for row in reader:
# #     #     students.append({"name": row[0], "home": row[1]})
# #     for name, home in reader:
# #         students.append({"name": name, "home": home})

# # with csv header
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     # "name" and "home" come from csv header
#     # allows csv to be written and home,name as long as the header is updated
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#         # students.append(row)


# for student in sorted(students, key=lambda x: x["name"]):
#     print(f"{student['name']} is from {student['home']}")

# ==========================================

import csv

name = input("name: ")
home = input("home: ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)  # Auto handles comma in input
    writer.writerow([name, home])  # must be in order of csv

# with open("students.csv", "a") as file:
#     # must be in order of csv
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})  # any order
