
# collections

# create an empty list? Array
my_list = []
my_list2 = list()

# print(my_list)

# create a list with numbers 1, 2, 3, 4, 5
numbers = [1, 2, 3, 4, 5]
# numbers2 = list(1, 2, 3, 4, 5)

# add an element 24 to lst1
numbers.append(24)

# add an element 12 to the start of lst1
# print(numbers)
# print(lst1)

# # print all values in lst2
# print(lst2)
# print(numbers[2])
# print(lst1[0])
# print(lst1[1])
# print(lst1[2])
# print(lst1[3])
# print(lst1[4])

# loop over the list using a for loop
# for number in numbers:
#     print(number)

# for i in range(0,6):
#     print(numbers[i])

# # while loop
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i +=1


# List Comprehensions

# Create a new list containing the squares of all values in 'numbers'
numbers = [1, 2, 3, 4]
squares = [num * num for num in numbers]

# for num in numbers:
#     square.append(num*num)
# print(numbers)
# print(squares)

# Filtering with a list comprehension
evens = [num for num in numbers if num %2 == 0]
# for num %2 ==0:
#     evens.append(num)

# create a new list of even numbers using the values of the numbers list as inputs
# print(evens)

# create a new list containing only the names that start with 's'
# make sure they are capitalized (regardless of their original case)
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy"]
s_names = [name.capitalize() for name in names if name[0].lower()=='s']
print(s_names)

# Dictionaries

# Create a new dictionary

# empty
d = {}

# key value pairs
d2 = {
    "goooooogle": "Tom",
    (12, 23, 4): 41, 
    [23, 3, 4]: "Bob"
    "age": "Bob"
}

# access an element via its key
print(d2["name"]) #0(1)
print(d2[1]) #0(1)




# Lets think about Tuples?
# this of an imutable list --> the tuple
# good for constant values
'''
List comprehensions are fast. Useful if you are looping through huge data sets, for example. Noticeably faster than a hand written loop that does the same thing for a large enough N.
((This might be an interview question. “How do you speed this up?))
'''