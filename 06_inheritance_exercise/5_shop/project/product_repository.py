from project1.product import Product


class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_to_search):
        for product in self.products:
            if product.name == product_to_search:
                return product

    def remove(self, product_to_remove):
        for product in self.products:
            if product.name == product_to_remove:
                self.products.remove(product)

    def __repr__(self):
        output = list(f'{product.name}: {product.quantity}' for product in self.products)
        return '\n'.join(output)
