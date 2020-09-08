# lets write a store class with a name and categories

class Store:
    def __init__(self, name, categories):
        #attributes
        self.name = name
        self.categories = categories

    #how can we represent this class data as a string?
    def __str__(self):
        ret = f"{self.name}\n"
        for i, c in enumerate(self.categories):
            ret += " " + str(i + 1) + ": " + c + "\n"
        ret += " " + str(i + 2) + ": Exit"

        return ret

    def __repr__(self):
        return f"Store({self.name}, {self.categories})"

# difference between __repr__ and __str__

"""
rep is used for devs and str is used for users
Bob's Emporium
 1: False Legs
 2: Baseball Bats
 3: Fruit

Store(Bob's Emporium, ['False Legs', 'Baseball Bats', 'Fruit'])
Shows developer what it looks like
"""