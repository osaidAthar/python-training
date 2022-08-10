# ********************************************************* #
# Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#  Evaluate Values and Variables

# Evaluate a string and a number:
print(bool("Hello"))
print(bool(15)) 

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Most Values are True

# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False

# The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Functions can Return a Boolean

# Print the answer of a function:
def myFunction() :
  return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# ********************************************************* #