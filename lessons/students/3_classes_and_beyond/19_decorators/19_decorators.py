import datetime

"""
Learning about class decorators and object methods.
"""

#  TITLE: Section 1 - Prerequisite to Decorators

# In Python, decorators are used to add new functionality to existing objects without modifying
# their structure. With this in mind, it is important to remember that functions are considered
# "first class objects", meaning they can be passed as an argument, returned from a function call,
# and assigned to a variable.

# It is important to know the capabilities of functions in Python. To better understand how
# decortators work, we will use examples that demonstrate the different abilities related to
# functions.

# Like other obects in Python, functions can be assigned to variables. Below is an example of a
# simple function being assigned to a variable.

def greeting():
  """A function that creates a greeting."""
  name = input("What is your name? ")
  print(f"Hello {name}!")

# We can store the function "greeting()" in a variable called "hello".
hello = greeting # Notice the syntax here and how the parenthesis are not included in the value.

# Now "hello" can be called in the same way "greeting()" would be.
hello()

# Functions can also be defined within other functions. Below, we are defining the function
# "do_math()" which will have a nested function, "multiply()". The function "multiply()" will be
# called if the argument passed is a number greater then 10.

def do_math(num):
  """A function that will do some math."""
  print("'do_math()' was called.")

  def multiply(num):
    print("'multiply()' was called.")
    new_num = num * 2
    return new_num
  
  if (num > 10):
    final = multiply(num)
  else:
    final = num
  return final


# When "do_math()" is called, the nested function "multiply()" will be called if the provided
# argument is greater than 10. Print statements are being used to log the control of the original
# function call.

print(f"final: {do_math(11)}")

# Up to this point, we have only seen objects such as strings, integers, and lists passed as
# arguments in function calls. Functions can also be passed as an argument in function calls.

def adder(num): # This function will be called by "call_add_function()".
  print("'adder()' was called.")
  return num + 10

def call_add_function(func):
  print("'call_add_function()' was called.")
  num = 96
  return func(num) # Functions can be used in the return statement too.

print(call_add_function(adder))

# Lastly, an important concept in decorators is "closure". Closure is when a nested funtion has
# access to a variable in the outer scope of an enclosing function. Below is an example of this
# concept.

def greeting():
  """Enclosing Function"""
  name = input("What is your name? ")

  def greeting_printer():
    """Nested Function"""
    print(f"Hello {name}!") # The variable "name" is from outside the local scope of
                            # "greeting_printer()".
  greeting_printer()

greeting()
  
####################################################################################################

# TITLE: Section 2 - Decorators

# As a reminder, decorators are used to add new functionality to existing objects without
# modifying their structure. In the next example, we will demonstrate how to manually create a
# decorator in Python.

# Below is the function "lowercase_decorator()" that takes a function as an argument. Then the
# nested function "wrap()" will call the passed function and convert all characters in the given
# string to lowercase.

def lowercase_decorator(function):
  """This is a custom decorator."""
  def wrap():
    """
    This inner function will call the function passed as a parameter
    and modify its return value to be lower case.
    """
    func = function()
    lower = func.lower()
    return lower
  return wrap

# Below is a function that will be used as the argument in the function call of
# "lowercase_decorator()".

def all_caps_greeting():
  """This method returns the greeting, "HELLO WORLD"."""
  greeting = "HELLO WORLD"
  print(f"'greeting' before it is decorated: {greeting}.")
  return greeting

# Below we are storing our decorator function call as an argument into the variable "decorator".

decorate = lowercase_decorator(all_caps_greeting) # The decorator function wraps the function being
                                                  # decorated.
print(f"'greeting' after it is decorated: {decorate()}.") # Since the variable "decorate" is being
                                                          # used to store a function, parenthesis
                                                          # are needed to access its functionality.

# Python provides a simple way to call a function with a custom decorator. The pythonic way to use
# a decorator is with the syntax "@decorator_name" above the function definition you want decorated.
# Below we will redefine "all_caps_greeting()" to show how to decorate a function.

@lowercase_decorator
def all_caps_greeting():
  """This method is decorated with the "@lowercase_decorator" decorator."""
  greeting = "HELLO WORLD"
  return greeting

# Now when "all_caps_greeting()" is called, the decorator is automatically called. The expected
# result is for "hello world" to be printed to the terminal.
print(f"HELLO WORLD, but decorated: {all_caps_greeting()}")

#TODO: Section 1 of TODO 19 (8 minutes for students, 3 minute demo)

####################################################################################################

# TITLE: Section 3 Getters and Setters

# In past lessons, we have used dot (.) notation to get and set attributes for class objects. This
# is good for simple programs, but when working on more complicated projects it is likely that you
# will need to restrict the use of invalid values. In many cases as a software developer you will be
# contributing to an existing code base that already inlcudes thousands of lines of code. Creating
# new methods for getting and setting attributes is tedious and leaves room for error. However,
# Python provides an easy way to avoid having to do so with the built-in "@property" decorator.

# The "@property" decorator refers to the built-in "property()" function that is used to create a
# "property" object. The syntax for this function is "property(getter_function, setter_function)".
# A deleter function can also be passed as an argument. As we said previously, using the decorator
# makes it easier to handle older code and is more readable as well.

# Below we will define the class "Sneaker" to demonstrate the use of the "@property" decorator.
class Sneaker:
  # We will initalize one (1) private instance attribute of "price". As we learned in the last
  # lesson, this restricts the attributes access to within the class.
  def __init__(self, price):
    """ Initializing instance attributes """
    self.__price = price

  # The "@property" decorator is used here to indicate that we are definining a property. This will
  # act as the "getter".
  @property
  def price(self):
    """ Provides access to the private attribute "price" """
    return self.__price

  # Below, we are using "@price.setter" is a setter method for the "@price" property.
  @price.setter
  def price(self, new_price):
    """ Initializing instance attributes """
    if (new_price > 0 and isinstance(new_price, float)):
      self.__price = new_price
    else:
      print("Please enter a valid price of your sneaker.")

jordan1 = Sneaker(400.00) # This is an instantiation of Sneaker.

# Notice the getter and setter methods share the same name as the private "price" attribute. Now
# instead of calling the method with the syntax "price(new_price", we simply set the "price"
# attribute of the class instance equal to a new value. If the new value is deemed invalid by the
# method, then a message will be ouput to the terminal.

print(f"The current price of the shoe is ${jordan1.price}.")

# Below we are changing the value of the "price" attribute using the settor method.
jordan1.price = 500.00
print(f"The new price of the shoe is ${jordan1.price}.")

# Now we are setting the value of the "price" attribute to an invalid value, which will cause the
# "else" statement to be executed and print an error statement to the terminal.

jordan1.price = -400.00

# As a reminder, getters and setters are used to access and manipulate private attributes in a given
# class.

#TODO: Section 2 of TODO 19 (10 minutes for students, 5 minute demo)
