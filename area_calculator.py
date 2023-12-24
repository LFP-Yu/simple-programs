# *********  Area Calculator  *********
# What this program would do:
#   Ask the user to enter the lengths of all three sides of a triangle
#   Calculate the area of the triangle
#   Calculate the half of sum of the three sides and store it in variable s
#   If the input lengths could form a valid triangle 
#     (i.e. sum of any two sides should be greater than the third one, or
#            half of sum of all the three sides should be greater than any one side),
#       Calculate the area of the triangle using the formula:
#         area = √(s(s-a)*(s-b)*(s-c)) where a,b,c are the three sides of the triangle
#       Print out the area
#   Otherwise, print an error message and stop the program


# ********  START OF CODE  ********


# Accepting lengths of the three sides of a triangle from user
while True:
    try:
        side1 = float(input("Enter the first side of the triangle: "))
        side2 = float(input("Enter the second side of the triangle: "))
        side3 = float(input("Enter the third side of the triangle: "))
    except:
        print('INPUT ERROR: only numeric data are accepted here.')
        print('Please enter all the data again.')
    else:
        break

# Calculate the area and print it out if it is a valid triangle
import math
s = (side1 + side2 + side3)/2
if s > side1 and s > side2 and s > side3:
    area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
    print("The area is {:.2f}.".format(area))

# Otherwise, print an error message
else:
    print ("INPUT ERROR: The input lengths could not form a triangle.")


# ********  END OF CODE  ********
