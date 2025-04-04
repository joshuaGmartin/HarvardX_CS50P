# call on class creates an object
# these methods are instance methods (per object). as opposed to class methods
class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name  # runs name check in setter
        # self._house would set actuall value, allowing bypass house check
        self.house = house  # calls setter method
        self.patronus = patronus

    # allows calls on object itself to be seen
    def __str__(self):
        return f"{self.name} from {self.house} with a(n) {self.patronus}"

    # Getter house
    @property
    def house(self):
        return self._house  # instance variable

    # Setter house
    @house.setter
    def house(self, house):
        # error handle in setter
        if house not in ["Gryff", "Huff", "Ravenclaw", "Slyth"]:
            raise ValueError("Invalid house")

        # because setter is called in init, _house exists immediately
        self._house = house

    # Getter name
    @property
    def name(self):
        return self._name

    # Setter name
    @name.setter
    def name(self, name):
        if not name:  # cancel create obj
            raise ValueError("Missing name")
        self._name = name

    # method is a func in a class
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case _:
                return "❓"


def main():
    # name = input("Name: ")
    # house = input("House: ")
    # name, house = get_student()
    # print(f"{name} from {house}")

    # student = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"  # not assignable as tuple
    # print(f"{student[0]} from {student[1]}")

    student = get_student()
    # student.house = "Slyth"  # python knows to use setter method
    # student.house = "test"
    # _ is a convention, not a constraint. Python says, "play nice"
    student._house = "test"
    # print(f"{student.name} from {student.house}")
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    # name = input("Name: ")
    # house =  input("House: ")
    # name = "Harry"
    # house = "Gryff"
    # return (name, house)

    # tuple: good for programming defensively - immutable
    # return "Harry", "Gryff"
    # return "Padma", "Gryff"

    # list = mutable
    # return ["Harry", "Gryff"]
    # return ["Padma", "Gryff"]

    # dict: no longer rely on order
    # return {"name": "Harry", "house": "Gryff"}
    # return {"name": "Padma", "house": "Gryff"}

    # create own data type with classes
    # student = Student()
    # # add attributes (instance variables) with dot notation
    # student.name = "Harry"
    # student.house = "Gryff"

    # return student

    # name = "Harry"
    # house = "Gryff"
    # patronus = "Stag"
    # name = "Draco"
    # house = "Slyth"
    # patronus = None
    name = "Ron"
    # name = None
    house = "Gryff"
    # house = "not a house"
    patronus = "Otter"
    return Student(name, house, patronus)

    # name = None
    # house = None
    # return Student(name, house)

    # return Student()


if __name__ == "__main__":
    main()
