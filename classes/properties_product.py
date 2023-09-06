class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError
    #     self.__price = value
    # price = property(get_price, set_price)


product = Product(40)
print(product.price)
