score = int(input("Score: "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# chain conditionals like in maths
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score <= 90:
#     print("Grade: B")
# elif 70 <= score <= 80:
#     print("Grade: C")
# elif 60 <= score <= 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

# must use elif here
if 90 <= score:
    print("Grade: A")
elif 80 <= score:
    print("Grade: B")
elif 70 <= score:
    print("Grade: C")
elif 60 <= score:
    print("Grade: D")
else:
    print("Grade: F")
