from category import MenuCategory
from dish import Dish
import os

class Menu:
    def __init__(self):
        self.categories: list[MenuCategory] = []
        self.dishes: dict[str, Dish] = {}

    def find_dish(self, name: str):
        return self._dishes.get(name.lower())


    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if not isinstance(value, list):
            raise TypeError("Categories must be a list of MenuCategory")
        if not all(isinstance(cat, MenuCategory) for cat in value):
            raise ValueError("All items in categories must be MenuCategory")
        self._categories = value

    def load_from_file(self, filename: str):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Menu file '{filename}' not found.")

        self.categories = []
        self._dishes = {}

        with open(filename, 'r', encoding='utf-8') as file:
            current_category = None

            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("[") and line.endswith("]"):
                    category_name = line[1:-1]
                    current_category = MenuCategory(category_name)
                    self.categories.append(current_category)
                elif current_category:
                    try:
                        name, price = line.split(",")
                        dish = Dish(name.strip(), float(price.strip()))
                        current_category.add_dish(dish)
                        self._dishes[dish.name.lower()] = dish
                    except ValueError:
                        print(f"error: {line}")

        return self._dishes.get(name)

    def display_menu(self):
        for category in self.categories:
            print(category)
            print()