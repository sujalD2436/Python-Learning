# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Sujal", 19)
happy_birthday(20, "John") # Parameters are reversed here
happy_birthday("Drishti", 12)

# The passed things are arguments and the received end on function are parameters
# Parameters are to be in order for proper management