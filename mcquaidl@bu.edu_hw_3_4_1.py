# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/22/18
Homework 3, Question 4.1
Algebra: solve quadratic equations
"""

import math

try:
    user_input = input('Enter a, b, c: ')

    user_input_valid= user_input.split(',')
    a = float(user_input_valid[0])
    b = float(user_input_valid[1])
    c = float(user_input_valid[2])
    
    discriminant = (b**2 
                    - (4
                    *a
                    *c))
     
    if discriminant > 0:
        root_1 = ((-b
              + math.sqrt(discriminant))
              / (2
                 *a))
    
        root_2 = ((-b
              - math.sqrt(discriminant))
              / (2
                 *a))   
        print('The roots are {:.6f} and {:.6f}' .format(root_1, root_2))
        
    elif discriminant == 0:
        root_1 = ((-b
              + math.sqrt(discriminant))
              / (2
                 *a))
        print('The root is {} ' .format(root_1))

    else:
        print('The equation has no real roots')

except:
    print('Please enter valid numbers for a, b, and c')