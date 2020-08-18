"""
This is an introduction to basic math and imports in Python
"""
# TITLE: Section 1:
# Math in Python works exactly as you'd think it should. It's just like using a calculator,
# except you can store equations in variables. Below are basic mathematical operations you have 
# seen in standard algebra classes.
addition = 2 + 2 # This is addition
subtraction = 10 - 5 # This is sutraction
multiplication = 3 * 4 # This is multiplication
division = 12 / 4 # This is division
exponents = 2 ** 2 # This is finding exponential value (2^2 or 2 squared)

# IMPORTANT:
# In python 2, division of whole numbers always returned a whole number,
# but in python 3, they return float values.

# The "%" is called the modulo operator. The modulo operator is used to return the remainder
# of one number in the next. In the below example, 9 goes into 120 13 times with a remaineder of 3.
remainder = 120 % 9
print("Math Section One")
print(f"addition: {addition}, subtraction: {subtraction}, multiplication: {multiplication}, division: {division}, exponents: {exponents}, remainder: {remainder}.")

# Let us not forget, variables can be changed! Lets reassign multiple variables in one line.
# Use Lesson 2 Section 2 if you need a reminder on setting multiple variables in a line.
addition, subtraction, multiplication = 4 + 4, 20 - 6, 2 * 2

print("Lets see if our variables changed.")
print("addition: ", addition, "subtraction: ", subtraction, "multiplication: ", multiplication)

####################################################################################################

# TITLE Section 1.1:

# Math in Python follows all the same rules as if you were completing a problem in
# your notebook or with a scientific calculator. In other words, Python follows PEMDAS.
# Let's test out some examples.

eq1 = 4 * 12 - 10
eq2 = (6 + 3) ** 2
eq3 = 7 + 2 / 2 - 3

print(f"we expect eq1 to equal 38. Python gives us {eq1}")
print(f"we expect eq1 to equal 81. Python gives us {eq2}")
print(f"we expect eq1 to equal 5. Python gives us {eq3}")

# IMPORTANT:
# Remember when you divide, the output will be a float. If you want an integer,
# you should us type conversion.
print(f"we expect eq1 to equal 5. Python gives us {int(eq3)}")


####################################################################################################

# TITLE Section 1.2:
# Here is a new concept we haven't covered yet- constants! Constants are like variables,
# but they are typed in all caps and don't change. Variables can be manipulated and change,
# whereas constants must remain the same.

# For example, the corporate tax rate is 20%. Hence, that would be an example of a constant.
# You might also notice for company_profit, we use the int() function to convert the user input
# (a string) to an integer.
company_profit = int(input("How much money did your company make this year?: "))
CORPORATE_TAX_RATE = .20

# IMPORTANT:
# Here we see our first example of copmbining new concepts. A mathematical equation is set using a
# vaiable and a constant. This is important to recognize because company_profit can change which
# will therefore change the value of taxes_paid.
taxes_paid = company_profit * CORPORATE_TAX_RATE
print(f"I paid ${taxes_paid:.2f} dollars in taxes for my business.")

# If you do calculations between a integer and float, the output is a float.
summation = 3 + 3.0 # Summation will now equal 6.0

# Let's say you want to add to the variable summation. You want to increment it by one, for
# whatever reason. There's one way to do this that is not the greatest.
# Lets do it that way first.
summation = summation + 1 # Summation will now be 7.0

# Using += will add whatever value comes after to the variable, then reassign the variable
# to that new value. Since summation was 7.0 and we use += 2, the value of summation after
# this line will be 9.0.
summation += 2 # summation will now equal 9.0

# To the same tone, you can decrement with -=. Let's see how that looks.
summation -= 3

# TODO: Section 1 of TODO 4

# ####################################################################################################

# TITLE: Section 2:
# Python makes it easy to find things like min and max too. Luckily there are built in functions we can
# use. Below is a list of random numbers we are going to work on to show some examples.
number_list = [13, 27, 4, 12, 39, 100]

# IMPORTANT:
# Certain functions have return values that can be be placed in print statements, and their return
# values will be printed as a string when using f shorthand.

# To find the smallest number, or minimum, in a list, we can use the built in function: min().
print(f"The min of number_list is {min(number_list)}")

# To find the largest number, or maximum, in a list, we can use the built in function: max().
print(f"The max of number_list is {max(number_list)}")

# To find the summation of all the numbers in a list, we can use sum(). This is beneficial for when
# you have a bunch of numbers and don't want to add them all together with a bunch of plus signs.
print(f"The sum  of number_list is {sum(number_list)}")

# If you remember from math class, the absolute value of a number is the positive of any number.
# So the absolute value of 10 and -10 are both 10.
neg = -10
pos = 10
print(f"The absolute value of {neg} is {abs(neg)}.")
print(f"The absolute value of {pos} is {abs(pos)}.")

# The same concept applies to floats as well!
neg_float = -49.232
pos_float = 49.232
print(f"The absolute value of {neg_float} is {abs(neg_float)}.")
print(f"The absolute value of {pos_float} is {abs(pos_float)}.")

# TODO: Section 2 of TODO 4

####################################################################################################	

# We also have the math package/module from python. Python has built in tools that we	
# can import and use to help us in mathematical operations. Normally imports go at the	
# TOP of a file, but we will put it here to consolidate the lesson.	

import math	

# Now that we have the math package imported, we can use methods attached to the module. One	
# such method we can import is is pow() 👊🏿. This is used to check a mathematical power.	
# For example, pow(3, 3) would be three raised to the third power, which is 27.	

doing_math_pow = math.pow(3, 3)	

# The ** exponent is the equivalent of the above.	
doing_math_exp = 3**3	

print('Here is the output of the math module example: ', doing_math_pow)	
print('Here is regular 3**3 without the math package: ', doing_math_exp)	

# As you can see, the math package result returns a float whereas the normal math	
# operation returned an integer. Nothing interesting here, just a lil' note.
