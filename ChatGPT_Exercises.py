import math
"""
Author: Jhenifer
Purpose: ChatGPT Exercises
"""

# Convert from km to miles
# 1km= 0.621371 
# Display the result to two decimal places.

km = float(input(f"How many km have you driven? I'll tell you the miles: "))
miles = (km * 0.621371)
print()
print(f"You've driven {miles:.2f} miles.")


# -------------------------------------------------------------------------------------------------------------------


# Convert from pounds to kg
# 1 pound (lb) = 0.453592
# Display the result to two decimal places.

pound = float(input(f"Enter how many pounds you have: "))
kg = 0.453592 * pound
print()
print(f"You have got {kg:.2f} kilos. ")


# -------------------------------------------------------------------------------------------------------------------


# Calculate the area of a circle
# Area = 𝜋 × radius 2
# # Display the result to two decimal places.

radius = float(input(f"Enter the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area:.2f}")


# -------------------------------------------------------------------------------------------------------------------


# Calculate simple interest. 
# The formula for simple interest is: 
# Simple Interest = p * r * t / 100
# where P is the principal amount, 
# R is the rate of interest, and T is the time in years. Display the result to two decimal places.

p = float(input(f"What is your P? "))
rate_interest = float(input(f"What is your R? "))
time = float(input(f"How many years? "))
simple_interest = p * rate_interest * time / 100
print(f"Your simple interest is {simple_interest:.2f}" )