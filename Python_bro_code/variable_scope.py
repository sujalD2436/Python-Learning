# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 300  # Local scope
    print(x)
    
def func2():
    x = 100  # Local scope
    print(x)
    
func1()
func2()

def func1():
    x = 300  # Enclosed scope
    def func2():
        print(x) # Accessing the enclosed variable
    func2()
func1()

def func1():
    print(x)  # Accessing the global variable

def func2():
    print(x)  # Accessing the global variable
    
x = 3

func1()
func2()

from math import e

def func1():
    print(e)
    
print(e)  # Accessing the built-in variable
func1()