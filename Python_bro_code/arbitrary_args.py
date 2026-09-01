# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY

# *args => creates a tuple of arguments that are passed
# Here, *<name> => {<name>} can be anything you want...

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4)) # Now, it can accept as many number of arguments
print("----------------------------------------------------------------")
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Sujal", "Samir", "Drishti", "Anuva", "Das")
print()
print("----------------------------------------------------------------")

def print_address(**kwargs):
    print(type(kwargs)) # kwargs stores as a dictionary
    # key=> .keys and value=> .values
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Hariom Colony, Chinchpada",
              apt="304",
              city="Kalyan",
              state="Maharashtra",
              zip="421306")
print("----------------------------------------------------------------")
# Yaha jaise likah hei, keyword then positional only hoga naaki vice-versa
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="124 Conch Street",
               #apt="Apt. 2",
               #pobox="PO Box 1234",
               city="Detroit",
               state="Michigan",
               zip="54321")