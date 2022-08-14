# ********************************************************* #
# Modules

# Create a Module
import mymodule
mymodule.greeting("Jonathan")

# Variables in Module
import mymodule
a = mymodule.person1["age"]
print(a)

# Naming a Module

# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules

# Import and use the platform module:
import platform
x = platform.system()
print(x)

# Using the dir() Function

# List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)

# Import From Module

# Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"])



# ********************************************************* #