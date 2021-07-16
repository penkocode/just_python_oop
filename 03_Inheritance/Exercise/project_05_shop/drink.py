from project_01_wild_cat_zoo.product import Product


class Drink(Product):

    def __init__(self, name: str):
        super().__init__(name, 10)
