# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/5/18
Homework 5, Question 15.1
Sum the digits in an integer using recursion
"""

def sumDigits(n):
    """
    Recursive function where the digits in an integer are added together
    
    param 1: user-entered integer
    """
    if n == 0:
        return 0
    else:
        total_sum = (n % 10) + sumDigits(n // 10)
    
    return total_sum
        
def recursiveOutput():
    """
    Ask the user for an input, and display the recursive output
    
    param 1: user input
    """
    try:
        user_input = int(input('Please enter an integer: '))
        total = sumDigits(user_input)
        print('The sum of the numbers within {} is {}'\
              .format(user_input, total))  
    except:
        print('User input is not an integer, please enter an integer.')#Check
        #to see if the usser input is an integer

if __name__ == "__main__": 
    recursiveOutput() #Call the matrix calculation function