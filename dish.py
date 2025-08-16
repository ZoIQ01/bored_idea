class Dish:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def __str__(self):
        return f"{self.name} — {self.price} UAH"


