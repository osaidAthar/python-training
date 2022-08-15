# ********************************************************* #
# Operators

# Python Operators
print(10 + 5)

# Python Arithmetic Operators
# Addition
x = 5
y = 3
print(x + y)

# Subtraction
x = 5
y = 3
print(x - y)

# Multiplication
x = 5
y = 3
print(x * y)

# Division
x = 5
y = 3
print(x / y)

# Modulus
x = 5
y = 3
print(x % y)

# Exponentiation
x = 5
y = 3
print(x ** y)

# Floor division
x = 5
y = 3
print(x // y)

# Python Assignment Operators

# =
x = 5
print(x)

# +=
x = 5
x += 3
print(x)

# -=
x = 5
x -= 3
print(x)

# *=
x = 5
x *= 3
print(x)

# /=
x = 5
x /= 3
print(x)

# %=
x = 5
x %= 3
print(x)

# //=
x = 5
x //= 3
print(x)

# **=
x = 5
x **= 3
print(x)

# &=
x = 5
x &= 3
print(x)

# |=
x = 5
x |= 3
print(x)

# ^=
x = 5
x ^= 3
print(x)

# >>=
x = 5
x >>= 3
print(x)

# <<=
x = 5
x <<= 3
print(x)

# Python Comparison Operators

# Equal
x = 5
y = 3
print(x == y)

# Not equal
x = 5
y = 3
print(x != y)

# Greater than
x = 5
y = 3
print(x > y)

# Less than
x = 5
y = 3
print(x < y)

# Greater than or equal to
x = 5
y = 3
print(x >= y)

# Less than or equal to
x = 5
y = 3
print(x <= y)

# Python Logical Operators

# (	Returns True if both statements are true)
x = 5
print(x > 3 and x < 10)

# (Returns True if one of the statements is true)
x = 5
print(x > 3 and x < 10)

# (	Reverse the result, returns False if the result is true)
x = 5
print(not(x > 3 and x < 10))

# Python Identity Operators

# (	Returns True if both variables are the same object)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# 	(Returns True if both variables are not the same object)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

# Python Membership Operators

# (	Returns True if a sequence with the specified value is present in the object)

x = ["apple", "banana"]
print("banana" in x)

# (	Returns True if a sequence with the specified value is not present in the object)

x = ["apple", "banana"]
print("pineapple" not in x)

# ********************************************************* #