class ShoppingBasket(object):
    def __init__(self, items=[]):
        self.items = items

    def total(self):
        return sum(map(lambda item: item.subtotal(), self.items))


