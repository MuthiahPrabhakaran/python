"""
My First Py Program
It describes the multi line comment
"""
print("Hello World") # Printing a string
print(100) # Printing number

greeting = "Hello "
print(greeting + "World")

happy_thought = "Happy "
print(happy_thought)

# Declaring Constants
PI = 3.14  # naming constants in capital letter. No other way to explicitly define constant. We can modify in python.
API_KEY = "xcdfdgsdfdws"


# Data types
text = "text" # string
number = -100 # integer - whole number
decimal = 3.14 # float - decimal number
complex_number = 8j # complex number

people = ["John", "Doe"] # list - can be altered
lotto_numbers = (1, 2, 3, 4, 5, 6) # duple - it can't be changed once created
numbers = range(1, 1000) # range - generates 1 to 999 here

users = {'user1': 'John Doe', 'user2': 'Tom'} # dictionary - similar to map in java
unique_numbers = {1, 2, 3, 3, 3, 4, 5} # set - keep only the unique numbers
frozen_set = frozenset({1, 2, 2, 3, 4, 5}) # immutable set

is_connected = False

is_empty = None # no value associated

# type hinting
name: str = "Mario" # explicitly mentioning the data types. If we assign number or other value here, python will let us know what is expected. But, no error will happen in that case.

# type conversion
"""
String can be concat with string in python. Same with number.
If the conversion doesn't make sense, it will throw error. Like converting an actual string to number
"""
name1 = 'John'
number1 = 10
result = name1 + str(number1)
print(result)
print(type(result)) # <class 'str'>

number_hundred = "100"
result = number1 + int(number_hundred)
print(result)

print(bool(1))
print(bool(0))
print(float("100.13"))

# integer - whole number - positive or negative
a = 1
b = 100
c = 17863483445
d = -10
print(a, b, c, d)
print(a + d)
e = 100_000_000 # formatting a number. underscore will be omitted
print(e)








