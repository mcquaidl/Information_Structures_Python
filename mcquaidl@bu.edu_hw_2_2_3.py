# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/15/18
Homework 2, Question 2.3
Convert feet into meters
"""

try:
    feet = float(input('Enter a value for feet: '))
        
    meters = (0.305
         * feet)
        
    print('{} feet is {} meters' .format(feet, meters))
    
except:
    print('Please enter a valid number')