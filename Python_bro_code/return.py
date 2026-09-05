# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

# return ke wajah se woh function hi woh return value ho jata hei basically

print(add(1, 2)) 
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

print("-----------------------------------------------------------------")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    
    return first + " " + last

full_name = create_name("sujal", "das")
print(full_name)