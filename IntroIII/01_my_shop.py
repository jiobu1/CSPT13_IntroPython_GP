# lets import what we need and start working on REPL
from store import Store

my_store = Store("Bob's Emporium", ["False Legs", "Baseball Bats", "Fruit"])

print(my_store)
print(repr(my_store))