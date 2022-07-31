import copy
from pickle import TRUE

# Constructing list
l=[]
l1 = list()
print(type(l),type(l1))

# ********************************************************* #

# Initializing list

l = [1,2,3,4,5]
l1 = list((1,2,3,4,5))
print(l,l1)

# ********************************************************* #

# ********************************************************* #

#List Slicing

newList = l[0:3] #it will give create new list with first three value
print(newList)

# Get all the Items After a Specific Position
my_list = [1, 2, 3, 4, 5]
print(my_list[2:])

# Get all the Items Before a Specific Position
my_list = [1, 2, 3, 4, 5]
print(my_list[:2])

# Get all the Items
my_list = [1, 2, 3, 4, 5]
print(my_list[:])

# ********************************************************* #

# ********************************************************* #

#Copying list
l2 = l1  #Sallow copy
shallowCopy = copy.copy(l1)
print(l2)
print(shallowCopy)
l1[1]=100 #Changes in main list will reflect in copied list
print(l2) #List is changed now
print("Shallow Copy",shallowCopy)

l3 = copy.deepcopy(l1) #Deep copy
l4 =l1[:] #Deep copy using slicing
print(l3)
print(l4)
l1[2]=300 #Changes will not reflect in copied list
print(l3)
print(l4)

# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# ********************************************************* #

# ********************************************************* #

#Sort list 

slist = ["orange", "mango", "kiwi", "pineapple", "banana"] # Sort the list alphabetically:
slist.sort()
print(slist)

# Sort Descending
slist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
slist.sort(reverse = True)
print(slist)

# Customize Sort Function
def myFunction(n):
    return abs(n - 50)

mlist = [100, 50, 65, 82, 23]
mlist.sort(key = myFunction)
print(mlist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reversed order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# ********************************************************* #

# ********************************************************* #

# Access List Items

slist = ["apple", "banana", "cherry"]
print(slist[1])

# Navigation index
slist = ["apple", "banana", "cherry"]
print(slist[-1])

slist = ["apple", "banana", "cherry", "apple", "banana", "cherry"] #Return list
print(slist[2 : 5])

# ********************************************************* #

# ********************************************************* #
# Change List Items

thislist = ["apple", "banana", "cherry"] # Change the second item:
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# ********************************************************* #

# ********************************************************* #

# Add List Items

thislist = ["apple", "banana", "cherry"] #Using the append() method to append an item:
thislist.append("orange")
print(thislist)

# Insert list

thislist = ["apple", "banana", "cherry"] # Insert an item as the second position:
thislist.insert(1, "watermelon")
print(thislist)

# Extend list

thislist = ["apple", "banana", "cherry"] # Add the elements of tropical to thislist:
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# tuple list 

thislist = ["apple", "banana", "cherry"] # Add elements of a tuple to a list:
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# ********************************************************* #

# ********************************************************* #

# Remove List Items

# Remove Specified Item
# The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"] # Remove "banana":
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"] # Remove the second item
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# ********************************************************* #

# ********************************************************* #

# Loop Lists
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"] 
for i in range(len(thislist)):
  print(thislist[i])

# Using a While Loop
# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  

# Looping Using List Comprehension
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# ********************************************************* #

# ********************************************************* #

# List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# The Syntax

# Condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Iterable
newlist = [x for x in range(10)] # You can use the range() function to create an iterable:
print(newlist)

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# ********************************************************* #

# ********************************************************* #

# Join list

# Join Two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# ********************************************************* #