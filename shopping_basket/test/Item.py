class Item(object):
    def __init__(self, price, quantity):
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.price * self.quantity
