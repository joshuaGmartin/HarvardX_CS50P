class Package:
    def __init__(self, id, sender, reciever, weight):
        self.id = id
        self.sender = sender
        self.reciever = reciever
        self.weight = weight

    def __str__(self):
        return f"Package {self.id}: {self.sender} to {self.reciever}, {self.weight}kg"

    def calc_cost(self):
        return self.weight * 1.25


def main():
    # bad; too flexible
    # packages = ["p1: a to b, 10kg", "p2: b to c, 5kg"]
    packages = [
        Package(1, "Alice", "Bob", 10),
        Package(2, "Bob", "Carol", 5),
        Package(3, "Carol", "David", 3),
    ]

    for package in packages:
        print(package)
        print(f"Cost to ship: ${package.calc_cost()}")


main()
