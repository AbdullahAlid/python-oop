class Item:
    pay_rate = 0.8  # class level attribute

    def __init__(self, name: str, price: float, qty=0):
        assert price >= 0, f"Invalid price"
        assert qty >= 0, f"Invalid qty"

        self.name = name
        self.qty = qty
        self.price = price

    def calculate_total_price(self):
        return self.calculate_discount()*self.qty

    def calculate_discount(self):
        self.price *= self.pay_rate
        return self.price


item1 = Item("phone", 200, 7)
item1.pay_rate = 0.7
# print(item1.calculate_discount())
print(item1.calculate_total_price())

item2 = Item("laptop", 200, 7)
# print(item1.calculate_discount())
print(item2.calculate_total_price())


# item2 = Item("laptop", 800, 4)
# print(item2.calculate_total_price())

# print(item1.__dict__)
