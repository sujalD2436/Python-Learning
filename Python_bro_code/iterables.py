# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# list, tuple, dictionary, set, string are all iterable objects

numbers = [1, 2, 3, 4, 5] # list

for number in reversed(numbers):
    print(number, end="-")
    # Can use reversed, end="", etc.
print()

numbers = (1, 2, 3, 4, 5) # tuple 

for number in numbers:
    print(number, end=" - ")
print()

# Sets cannot be reversed because they are unordered collections    
fruits = {"apple", "banana", "cherry", "orange", "coconut"} # set

for fruit in fruits:
    print(fruit, end=" ")
print()

name = "Sujal Das" # string

for character in name:
    print(character, end="")
print()

my_dictionary = {"A": 1, "B": 2, "C": 3} # dictionary

# By default, iterating over a dictionary iterates over its keys and not the values
# To access values, use .values() method
# To access key-value pairs, use .items() method
for key in my_dictionary:
    print(key, end=" ") # prints keys by default
print()
for value in my_dictionary.values():
    print(value, end=" ") # prints values
print()
for key, value in my_dictionary.items():
    print(f"{key}: {value}") # prints key-value pairs
