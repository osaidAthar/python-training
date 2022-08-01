# ********************************************************* #

# Tuple

# Create a Tuple
thistuple = ("apple", "banana", "cherry") #Tuples allow duplicate values:
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry") #Print the number of items in the tuple:
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("apple",) #One item tuple, remember the comma:
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry") #String, int and boolean data types:
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# type()
mytuple = ("apple", "banana", "cherry") #What is the data type of a tuple?
print(type(mytuple))

# The tuple() Constructor
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

# ********************************************************* #

# ********************************************************* #

# Access Tuple Items

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing

# Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes

# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Range of Negative Indexes

# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# ********************************************************* #

# ********************************************************* #
# Update Tuples

# Change Tuple Values
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Remove Items

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Delet tuple

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# ********************************************************* #

# ********************************************************* #

# Unpack Tuples

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


# ********************************************************* #

# ********************************************************* #

# Loop Tuples

# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers

#  Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop

# Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# ********************************************************* #

# ********************************************************* #

# Join Tuples

# Join two tuples:
tuple1 = ("a", "b" , "c") #To join two or more tuples you can use the + operator:
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

# Multiply the fruits tuple by 2:
fruits = ("apple", "banana", "cherry") #If you want to multiply the content of a tuple a given number of times, you can use the * operator:
mytuple = fruits * 2
print(mytuple)

# ********************************************************* #