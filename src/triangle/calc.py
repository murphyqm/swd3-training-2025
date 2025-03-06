# Module to calculate the hypotenuse of a right-angled triangle
# Will have two functions, one to get the squares of the opp and adj
# One to calculate the square root of those added together
# a**2 + b**2 = c**2
# need to import numpy, etc.

# Function to get the squares of opp and adj
# Inputs/args: opp and adj (a and b)
# Outputs/returns: a**2 and b **2

def squares(opp, adj):
    opp_sq = opp**2
    adj_sq = adj**2
    return opp_sq, adj_sq

# Function to calculate the sqrt of those added
# Input/args: a**2 and b**2
# Output/return: c or hypotenuse

def hypot(opp_sq, adj_sq):
    sum_o_a = opp_sq + adj_sq
    sqrt = (sum_o_a)**0.5
    return sqrt
    