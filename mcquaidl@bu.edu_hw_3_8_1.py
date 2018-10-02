# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/22/18
Homework 3, Question 8.1
Check SSN
"""

def main():
    """
    Return whether the user entered a valid SSN
    
    Input param: user_input
    """
    
    #Prompt the user to enter the SSN
    user_input = input('Please enter a Social Security number in the\
 format ddd-dd-dddd (where \"d\" is a digit): ')

    if isValidSSN (user_input):
        print('Valid SSN')
    
    else:
        print('Invalid SSN')

#Check to see if the string is a valid SSN
def isValidSSN (user_input):
    """
    Validates whether the user entered a valid SSN
    Input param: user _input utilized from the previous function
    """
    
    #breakout the SSN entered into 3 parts
    user_input_valid= user_input.split('-')
    one_thru_three = user_input_valid[0]
    four_thru_five = user_input_valid[1]
    six_thru_nine = user_input_valid[2]
    
    #Does the text entered equal the expected number of characters
    if (len(user_input)) != 11:
        return False #Not a valid SSN
        
    #Does the first string have 3 characters
    if (len(one_thru_three)) != 3:
        return False #Not a valid SSN
    
    #Does the first string only have numbers
    if one_thru_three.isdigit() == False:
        return False #Not a valid SSN
    
    #Does the second string have 2 characters
    if (len(four_thru_five)) != 2:
        return False #Not a valid SSN
    
    #Does the second string only have numbers    
    if four_thru_five.isdigit() == False:
        return False #Not a valid SSN
    
    #Does the third string have 4 characters
    if (len(six_thru_nine)) != 4:
        return False #Not a valid SSN
    
    #Does the third string only have numbers
    if six_thru_nine.isdigit() == False:
        return False #Not a valid SSN
    
    return True #Input is a valid SSN

main() #Call the main function to print outcome