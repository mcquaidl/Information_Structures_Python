# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/15/18
Homework 2, Question 2.1
Convert Celsius to Fahrenheit
"""

try:
    celsius = float(input('Enter a degree in Celsius: '))
        
    fahrenheit = ((9/5)
         * celsius
         + 32)
        
    
    print('{} Celsius is {} Fahrenheit' .format(celsius, fahrenheit))

except:
    print('Please enter a valid number')