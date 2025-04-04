# good to put class in own file (module) so other programs can use also
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod  # instantiates itself
    def get(cls):
        # input
        name = "Ron"
        house = "Gryff"
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
