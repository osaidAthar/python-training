# ********************************************************* #
# Datetime

# Python Dates
# Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)

# Date Output

# Return the year and name of weekday:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects

# Create a date object:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

# The strftime() Method

# Display the name of the month:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# ********************************************************* #