# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/15/18
Homework 2, Question 3.1
Geometry: area of a pentagon
"""

import math

try:
    radius = float(input('Enter the length from the center to a vertex: '))
    
    side_length = ((2
        * radius)
        *math.sin(math.pi/5))
    
    area = (((3 * math.sqrt(3))
            / 2)
            * math.pow(side_length, 2))
    
    print('The area of the pentagon is {}' .format(round(area, 2)))
    
except:
    print('Please enter a valid number')