pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius**2

# Check your answer
# q1.check()



########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
# q2.store_original_ids()
######################################################################

c = a
a = b
b = c

######################################################################

# Check your answer
# q2.check()



# 8 - (3 * 2) - (1 + 1)

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
to_smash = (alice_candies + bob_candies + carol_candies) % 3

# Check your answer
# q4.check()