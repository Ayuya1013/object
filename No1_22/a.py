class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def with_tax(self):
        return int(self.price * 1.1)

    def show(self):
        print(self.name, self.with_tax())

p = Product("りんご", 120)
p.show()
