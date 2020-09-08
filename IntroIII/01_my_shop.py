# lets import what we need and start working on REPL
from store import Store
from category import Category
from data_for_store import cats

my_store = Store("Bob's Emporium", [cats["legs"], cats["bats"], cats["fruits"], cats["special"]])

print(my_store)
# print(repr(my_store))

selection = 0

while selection != len(my_store.categories) + 1:
    selection = input("Please select the number of department. ")
    try:

        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print(f"Thanks for shopping at {my_store.name}")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection - 1])
        else:
            print("Please select a valid number")

    except ValueError:
        print("Pleaes enter your choice as a number. ")

    print(f"The user selected {selection}")