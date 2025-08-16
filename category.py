from dish import Dish

class MenuCategory:
    def __init__(self, name: str):
        self.name = name
        self.dishes: list[Dish] = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def __str__(self):
        output = f"--- {self.name} ---\n"
        output += "\n".join(str(dish) for dish in self.dishes)
        return output