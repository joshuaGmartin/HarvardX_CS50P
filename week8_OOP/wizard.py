# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house


# # feels redundant
# class Professor:
#     def __init__(self, name, subject):
#         # DRY!!!
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.subject = subject

# =============================================


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# inheritance class(super_class). Student inherits from Wizard
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # super refs Wizard
        self.house = house


# feels redundant
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


class Dean(Professor):
    def __init__(self, name, subject, school):
        super().__init__(name, subject)
        self.school = school


wizard = Wizard("Albus")
student = Student("Harry", "Gryff")
professor = Professor("Severus", "Def. DA")
dean = Dean("Dumbledor", "Nice magic", "Magic Arts")
