# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/8/18
Homework 5, Question 15.3
Compute greatest common divisor using recursion
"""

def calculateGCD(num1, num2):
    """
    Calculate the greatest common divisors between the two numbers entered
    
    param 1: user input
    param 2: user input
    """
    if 0 == num1 % num2:
        return num2
    return calculateGCD(num2, num1%num2)


def gcd():
    """
    Ask the user for 2 inputs, and determine the greatest common divisors
    between the two
    
    param 1: user input
    param 2: user input
    """
    try:
        user_input_1 = int(input('Please enter the first integer: '))
        user_input_2 = int(input('Please enter the second integer: '))
        
        gcd = calculateGCD(user_input_1, user_input_2)
        
        print('The greatest common divisor of {} and {} is {}'\
              .format(user_input_1, user_input_2, gcd))  
    except:
        print('User input is not an integer, please enter 2 integers to find\
 their greatest common divisor.')#Check to see if the user inputs are integers

if __name__ == "__main__": 
    gcd() #Call the matrix calculation function