# ********************************************************* #
# Strings
print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# Looping Through a String

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#  String Length
 
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# Check String

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)


# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
# ********************************************************* #
