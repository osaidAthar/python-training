# ********************************************************* #
# Try Except

# The try block will generate an exception, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

# Many Exceptions

# Print one message if the try block raises a NameError and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  

# Else

# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an exception

#  Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 

# ********************************************************* #