from dish import Dish


class Order:
    def __init__(self):
        self.items: list[Dish] = []
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        if not isinstance(value, list):
            raise TypeError("Items must be a list of Dish")
        if not all (isinstance(dish, Dish) for dish in value):
            raise ValueError("All items must be Dish")
        self._items = value

    def add_dish(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise TypeError("Only Dish instance can be added")
        self.items.append(dish)

    def total(self) -> float:
        return sum(dish.price for dish in self.items)

    def print_receipt(self):
        print("\n check:")
        for dish in self.items:
            print(f"- {dish.name}: {dish.price} UAH")
        print(f"\n total: {self.total()} UAH\n")