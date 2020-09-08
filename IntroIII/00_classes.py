# lets talk about classes

# holds data
# methods to act upon that data

# class called Vec2
# hold x and y as integers
# constructor that can take in x and y

# class Vec2 {
#     constructor(x, y) {
#         this.x = x;
#          this.y = y;
#     }
# }

# v = new Vec2(12, 23);

# this keyword === self keyword

# Encapsulation / Data Hiding
# only enforcement is by design
# __ method == Private
# _ method == Protected
#   method == Public

class Vec2: # Class keyword and then name for class
    def __init__(self, x, y): # initialize
        self.x = x  # self keyword refers to the actual address of itself
        self.y = y

    def __my_thing__(self, name): # technically should make methods private and then create a public way to access
        print(f"My name is {name}: ({self.x},{self.y})")

    def call_my_thing(self, name):
        self.__my_thing__(name)

# l = []
# l.__add__()

# l +

v = Vec2(12, 23)

v.call_my_thing("Bob")
#Utilizing public method to call a private method.

v.__my_thing__("Dave")


