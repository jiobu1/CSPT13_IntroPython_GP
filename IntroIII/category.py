# Lets create a class to hold our category data

class Category:
    def __init__(self, name): #, products ):
        self.name = name
        #self.products = propducts

    def __str__(self):
        return f"No products in {self.name}"