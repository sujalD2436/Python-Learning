# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# Positional arguments should be before keyword args
hello("Hello", title="Mr.", last="Das", first="Sujal")

# prefix any argument with the name of the parameter => Keyword args

hello("Hey There!", first="John", title="Mr.", last="Smith")

print("-----------------------------------------------------")

for x in range(1, 11):
    print(x, end=" ") # built-in functions
    # Here, end is also a keyword argument hence written like this

print("-----------------------------------------------------")

# here, sep is also keyword args
print("1", "2", "3", "4", "5", sep="-") # built-in functions