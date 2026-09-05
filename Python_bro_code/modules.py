# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in modules or custom modules)
#          useful to break up a large program into reusable separate files

help('modules')  # get help on modules
help('math')     # get help on a specific module

import math
# OR
import math as m  # {alias} # Mostly used when the module name is long
# OR
from math import pi # import a specific part of a module
# OR
from math import *  # import everything from a module

# We don't generally use the from wala method as it can create conflicts if two modules have a function with the same name

import example  # import custom module

result = example.pi
print(result)
result = example.square(3)
print(result)
result = example.cube(3)
print(result)
result = example.circumference(3)
print(result)
result = example.area(3)
print(result)