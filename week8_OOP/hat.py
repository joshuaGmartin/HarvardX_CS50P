import random


# use Classes to represent "real-world" entities
# only need one hat though, this allows multi hats
# class Hat:
#     def __init__(self):
#         self.houses = ["Gryff", "Huff", "Ravenclaw", "Slyth"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("Harry")


# ========================================================


class Hat:
    # like a global variable for the class (class variable, one copy is shared)
    houses = ["Gryff", "Huff", "Ravenclaw", "Slyth"]

    # same for shared methods (basically when you dont need self)
    @classmethod  # decorator (instance methods no need @)
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# like str.split("")
Hat.sort("Harry")
