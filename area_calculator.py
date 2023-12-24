# *********  Area Calculator  *********
# What this program would do:
#   Ask the user whether the triangle would be defined in SSS, SAS, or ASA
#   If SSS is chosen, then call the function area_sss, which will
#       Ask the user to enter the lengths of all the three sides of a triangle
#       Calculate the half of sum of the three sides and store it in variable s
#       If the input lengths could form a valid triangle 
#           Calculate the area of the triangle using the formula:
#             area = √(s(s-a)*(s-b)*(s-c)) where a,b,c are the three sides of the triangle
#           Print out the area
#       Otherwise, print an error message and stop the program
#   If SAS is chosen, then call the function area_sas, which will
#       Ask the user to enter the lengths of two sides and the angle in between of the triangle
#       If the input lengths could form a valid triangle 
#           Calculate the area of the triangle using the formula:
#             area = 0.5 * a * b * sin(p) where a,b are the sides and p is the angle of the triangle
#           Print out the area
#       Otherwise, print an error message and stop the program
#   If ASA is chosen, then call the function area_asa, which will
#       Ask the user to enter the lengths of two angles and the length of side in between of the triangle
#       If the input lengths could form a valid triangle 
#           Calculate the area of the triangle using the formula:
#             area = a² * sin(p) * sin(q) / (2 * sin(p + q)) where p,q are the two angles and a is the length of the side of the triangle
#           Print out the area
#       Otherwise, print an error message and stop the program

import math

# ********  START OF CODE  ********
triangle_desc = str()
while not triangle_desc in ['1','2','3']:
    print('Please choose how you would describe the triangle (1 - SSS, 2 - SAS, 3 - ASA):')
    triangle_desc = input('Your choice (1, 2 or 3): ')

# calculate the area of the triangle defined by side-side-side
if triangle_desc == '1':
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
    s = (side1 + side2 + side3)/2
    if s > side1 and s > side2 and s > side3:
        area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
        print("The area is {:.2f}.".format(area))
    
    # Otherwise, print an error message
    else:
        print ("INPUT ERROR: The input lengths could not form a triangle.")

# calculate the area of the triangle defined by side-angle-side
elif triangle_desc == '2':
    # Accepting lengths of the two sides and an angle of a triangle from user
    while True:
        try:
            side1 = float(input("Enter the first side of the triangle: "))
            side2 = float(input("Enter the second side of the triangle: "))
            angle = float(input("Enter the angle in degrees between the two lines of the triangle: "))
        except:
            print('INPUT ERROR: only numeric data are accepted here.')
            print('Please enter all the data again.')
        else:
            break

    # Calculate the area and print it out if it is a valid triangle
    if angle > 0 and angle < 180 and side1 > 0 and side2 > 0:
        area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
        print("The area is {:.2f}.".format(area))

    # Otherwise, print an error message
    else:
        print ("INPUT ERROR: The input could not form a triangle.")
    
# calculate the area of the triangle defined by angle-side-angle
else:
    # Accepting lengths of the two angles and the in-between side of a triangle from user
    while True:
        try:
            angle1 = float(input("Enter the first angle of the triangle in degrees: "))
            angle2 = float(input("Enter the second angle of the triangle in degrees: "))
            side = float(input("Enter the side between the two angles of the triangle: "))
        except:
            print('INPUT ERROR: only numeric data are accepted here.')
            print('Please enter all the data again.')
        else:
            break

    # Calculate the area and print it out if it is a valid triangle
    if angle1 > 0 and angle1 < 180 and angle2 > 0 and angle2 < 180 and (angle1+angle2) < 180 and side > 0:
        area = side*side*math.sin(math.radians(angle1))*math.sin(math.radians(angle2)) / (2*math.sin(math.radians(angle1)+math.radians(angle2)))
        print("The area is {:.2f}.".format(area))

    # Otherwise, print an error message
    else:
        print ("INPUT ERROR: The input could not form a triangle.")




# ********  END OF CODE  ********
