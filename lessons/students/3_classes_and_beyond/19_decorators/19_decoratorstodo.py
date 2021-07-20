"""
  Working with custom decorators and getters and setters.
"""


# TODO: Section 1.1

# Create a custom decorator called "uppercase_decorator". The "uppercase_decorator" should take
# a function as a paramter and modify each letter in its return value to be uppercase when used.



# TODO: Section 1.2

# Decorate the function below with the custom decorator "uppercase_decorator" and execute the file
# to test its functionality.


def greeting():
  long_greeting = "Hello world. It's a wonderful day today."


####################################################################################################

# TODO: Section 2.1

# Given the class "House" below, define a getter and setter using decorators. The setter should
# check that the new "price" of a house is greater than 0, less than 1000000, and an integer. Else
# print the statement, "Please enter a valid price of your home."

class House:

  def __init__(self, price):
    self.__price = price

  # TODO: Insert getter here



  # TODO: Insert setter here
  



# TODO: Section 2.2

# Create a new instantiation of "House" with a price of 200000 called "first_home".


# TODO: Section 2.3

# Try setting the price using the setter method defined in the "House" class of "first_home" to
# -100000. What is the expected outcome?


# TODO: Section 2.4

# Try setting the price using the setter method defined in the "House" class of "first_home" to
# 990100.10. What is the expected outcome?

# TODO: Section 2.5

# Try setting the price using the setter method defined in the "House" class of "first_home" to
# 400000. What is the expected outcome?
