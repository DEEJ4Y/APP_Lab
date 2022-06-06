# Rohit is new to python he needs to know
# a. How the warning messages can be displayed
# b. How the messages can be displayed with the values included
# c. How he can given values to the variables

import warnings

# Warning message
warnings.warn("This is a warning message")

# Message with variables
var1 = "var1"
# Variables can be printed using fstrings. Put the variables inside curly braces: {var1}
print(f'String with var inside: {var1}')

# Give values to variables
# <variable name> = <variable value>
var2 = "This is a variable value. It can be a string, a number, boolean, array or map"
print(var2)