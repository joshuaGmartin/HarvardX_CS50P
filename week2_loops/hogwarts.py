students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# ============================
# print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# ============================
# for student in students:
# print(student)

# ============================
# for i in range(len(students)):
#     print(i + 1, students[i])

# ============================

# key: value
student_and_house = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# ============================
# print(student_and_house["Hermione"])
# print(student_and_house["Harry"])
# print(student_and_house["Ron"])
# print(student_and_house["Draco"])

# ============================
# for student in student_and_house:
#     # print(student)
#     # print(student_and_house[student])
#     print(student, student_and_house[student], sep=" - ")


# ============================
# three keys
student_and_house_and_patronus = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in student_and_house_and_patronus:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# for i in range(len(student_and_house_and_patronus)):
#     print(student_and_house_and_patronus[i]["name"])
