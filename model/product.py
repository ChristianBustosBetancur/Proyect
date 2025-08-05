class Product:
    def __init__(self, name, quantity, price):
        self.Name = name
        self.Quantity = quantity
        self.Price = price


    def ToDict(self):
        return {
            "Name": self.Name,
            "Quantity": self.Quantity,
            "Price": self.Price
        }

    @staticmethod
    def FromDict(data):
        return Product(data["Name"], data["Quantity"], data["Price"])