# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/5/18
Homework 5, Question 6.5
Sort three numbers
"""
try:
    def displaySortedNumbers(num1, num2, num3):
        """
        Ask & Display the sorted numbers in increasing order 
        
        Param 1: first number
        Param 2: second number
        Param 3: third number
        """
        
        new_list = (num1, num2, num3)
        
        sort_list = sorted(new_list)
        
        print('The sorted numbers are {}, {}, {}'.format(sort_list[0],\
              sort_list[1], sort_list[2]))
    
    user_input = input('Enter Three Numbers: ')
    number_list= user_input.split(',')
    num1 = float(number_list[0])
    num2 = float(number_list[1])
    num3 = float(number_list[2])
    
    displaySortedNumbers(num1, num2, num3)

except: #Exception for non-numeric user inputs
    print('Please enter 3 valid numbers separated by a comma')