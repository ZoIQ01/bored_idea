import unittest
from dish import Dish
from category import MenuCategory
from menu import Menu
from order import Order
import os

class TestDish(unittest.TestCase):
    def test_dish_str(self):
        dish = Dish("Tea", 40)
        self.assertEqual(str(dish), "Tea — 40 UAH")


class TestMenuCategory(unittest.TestCase):
    def test_add_dish(self):
        category = MenuCategory("Starters")
        dish = Dish("Soup", 85)
        category.add_dish(dish)
        self.assertIn(dish, category.dishes)

    def test_category_str(self):
        category = MenuCategory("Drinks")
        category.add_dish(Dish("Tea", 30))
        expected = "--- Drinks ---\nTea — 30 UAH"
        self.assertEqual(str(category), expected)


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_menu.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("[Starters]\nBorscht,90\nSoup,85\n")
            f.write("[Drinks]\nTea,40\nCoffee,50\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_from_file(self):
        menu = Menu()
        menu.load_from_file(self.test_file)
        self.assertEqual(len(menu.categories), 2)
        self.assertEqual(menu.categories[0].name, "Starters")
        self.assertEqual(len(menu.categories[0].dishes), 2)

    def test_find_dish(self):
        menu = Menu()
        menu.load_from_file(self.test_file)
        dish = menu.find_dish("Tea")
        self.assertIsNotNone(dish)
        self.assertEqual(dish.name, "Tea")
        self.assertEqual(dish.price, 40)


class TestOrder(unittest.TestCase):
    def test_add_and_total(self):
        order = Order()
        order.add_dish(Dish("Borscht", 90))
        order.add_dish(Dish("Tea", 40))
        self.assertEqual(order.total(), 130)

if __name__ == '__main__':
    unittest.main()
