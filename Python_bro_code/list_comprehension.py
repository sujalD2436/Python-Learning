# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# Ye cheez ka shortcut is the above mentioned code=> Direct ho jaata hei ye sab...

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)
    
print(doubles)

# This is considered a shortcut to write the same big conditions

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
square = [z ** 2 for z in range(1, 11)]

print("Doubles: ", end="")
print(doubles)

print("Triples: ", end="")
print(triples)

print("Square: ", end="")
print(square)

print("----------------------------------------------")

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]

# OR => fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]

print(fruits)

print("----------------------------------------------")

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit[0] for fruit in fruits]

# OR => fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]

print(fruits)

print("----------------------------------------------")

numbers = [1, -2, 3, -4, 5, -6, -7, 8]

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

print("----------------------------------------------")

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)