"""
  Learning about built in Python methods and using them in custom objects.
"""

# TITLE: Section 1.1 - Accessing Doc Strings

# Documentation strings, or "doc strings" for short, provide a convenient way to leave descriptions
# of Python modules, classes, functions, and methods. Triple double quotes are used to declare a doc
# string as shown in the example below.

def addTen(x):
  """Adds 10 to a given integer or float."""
  x = x + 10
  return x

# There is a way to access the doc string in a Pythonic way as well by using the "__doc__" method.
# The syntax for access a function's doc string is "funciton.__doc__".

print(f"The doc string of addTen():\n{addTen.__doc__}")

# Doc strings are helpful in providing a greater understanding of the objects you've created to other
# programmers reading your code.

####################################################################################################

# TITLE: Section 1.2 - String Representation Methods

# Python provides two functions for showing string representations of objects as an output to the
# user, "str()" and "repr()". According to Python's documentation, the "str()" function is used to
# create an "informal" representation, meaning that the output is an easily read string. The
# "repr()" function is used to create a "formal" representation, meaning that the output is a valid
# Python expression that could be used to recerate an object with the same value.

# Using the datetime object, we are creating a date object of the date, "1/1/2021".
today = datetime.datetime(2021, 1, 1)

stringy = str(today)
print(stringy) # When printed, "stringy" will have the following output in the terminal:
               # "2021-01-11 00:00:00". This output is a string representation of the datetime
               # object that was created.

rep = repr(today)
print(rep) # When printed, "stringy" will have the following output in the terminal:
           # "datetime.datetime(2021, 1, 11, 0, 0)". This output is a representation of the Python
           # expression used to create the datetime object.

# These functions can also be used in custom objects to provide an output of its attributes as
# either a string or a Python expression. Below is a custom class called "Employee" that will be
# used to demonstrate this concept.

class Employee:
  """
  This is an object called Employee that has two attributes:
  name and start_date.
  """
  def __init__(self, name, start_date):
    self.name = name
    self.start_date = start_date

  def __repr__(self):
    """
    This method is used to return a valid Python expression
    that could be used to recreate a given instance of Employee.
    """
    return {"name": self.name, "start_date": self.start_date}

  def __str__(self):
    """
    This method is used to return an output that is easy to read
    in the form of a string.
    """
    return "(%s, %s)" % (self.name, self.start_date)

mark = Employee("Mark", datetime.datetime(2021, 6, 1)) # An instance of Employee is being
                                                       # instantiated.

# Below, the "__repr__()" and "__str__()" methods are being called to output the different
# representations of the attributes of "mark",

print(mark.__str__())
print(mark.__repr__())

####################################################################################################

# TITLE: Section 1.2 - Iterators

# In previous lessons, we have learned about iterators such as "for loops" and "while loops". An
# iterator is an object that can return data one element at a time. There are two special methods
# that every iterator object must implement, "__iter__()" and "__next()". The "iter()" function is
# used to call the "__iter__()" method and the "next()" function is used to call the "__next__()"
# method. Below is an example on how to use both functions.

food = ["apple", "ice cream", "hamburger"]

food_iter = iter(food) # The "iter()" function is used here to return an iterator from the list.

# Now the "next()" function will be used to iterate through the list, "food".
print(next(food_iter)) # The output of this will be "apple".
print(next(food_iter)) # The output of this will be "ice cream".
print(next(food_iter)) # The output of this will be "hamburger".

# As we learned in previous lessons, this can be easily accomplished with a "for loop" as well.
for f in food:
  print(f)

# It is possible to build a custom iterator in Python using the "__iter__()" and "__next__()"
# methods.

class PowThree:
    """This is an object to implement an iterator of powers of three."""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration # "StopIteration" is a Python exception that will be raised when
                                # an iterator is finished. Here, "StopIteration" is used to stop
                                # the iterator after it reaches its max value.

nums = PowThree(2) # Instantiating an instance of "PowThree".

iterator_nums = iter(nums) # Creating an iterable from the object, "nums".

# Below, we are using the "next()" function to iterate through "iterator_nums".
print(next(iterator_nums))
print(next(iterator_nums))
print(next(iterator_nums))

print(next(iterator_nums)) # The "next()" function raises the "StopIteration" exception because
                           # "nums.n" is greater than "nums.max".
