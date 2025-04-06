# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# # # list compomprehension
# # gryffindors = [
# #     student["name"] for student in students if student["house"] == "Gryffindor"
# # ]


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# # gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda g: g["name"]):
#     print(gryffindor["name"])
#     # print(gryffindor)

# ===========================================

# students = ["Harry", "Hermione", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# list comprehension for dictionaries
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# for gryffindor in gryffindors:
#     print(gryffindor)

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

# ===========================================

students = ["Harry", "Hermione", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

for i, student in enumerate(students):
    print(i + 1, student)
