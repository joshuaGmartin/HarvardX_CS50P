class Food:
    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts  # access class variable
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls([])
        food.hearts = hearts
        return food


def main():
    # mushroom_skewer = Food(["Mushroom", "Hearty Mushroom"])
    mushroom_skewer = Food.from_nothing(2)
    print(f"Heals {mushroom_skewer.hearts} hearts!")


main()
