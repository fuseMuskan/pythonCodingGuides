class Product:
    def __init__(self, price):
        self.price = price

    def calculated_total_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self,price,discount):
        super().__init__(price)
        self.discount = discount

        
    def calculated_total_price(self):
        total_price = self.price * (1 - self.discount)
        return total_price

def calculate_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.calculated_total_price()
    return total_price

products = [Product(100), DiscountedProduct(500, 0.2),  DiscountedProduct(750,0.2)]
print("Total Price:", calculate_total_price(products))