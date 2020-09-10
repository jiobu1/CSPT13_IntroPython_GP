# Lets create a class to hold our category data

class Category:

    def __init__(self, name, products):  #, products):
        self.name = name
        self.products = products

    def __str__(self):
        if len(self.products) == 0:
            return f"No Products in {self.name}"

        ret = f"{self.name}\n"
        for i, p in enumerate(self.products):
            ret += "    " + str(i + 1) + ": " + str(p.name) + " > " +  str(p.price) + "\n"
            ret += f"{p}\n"

        return ret

