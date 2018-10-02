# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/29/18
Homework 4, Question 10.3
Count occurrence of numbers
"""

try:
    user_input = input('Enter integers between 1 and 100: ')
    
    numbers = user_input.split(' ') #Separating numbers by spaces
    number_list = [int(x) for x in numbers] #Converting entries to integers
    count = [0 for i in range(1, 100)] #Establishing a 0 count for numbers 1 -100
    
    #Adding the count of numbers entered to the established count list above
    for user_num in number_list:
        count[user_num] += 1
    
    #Printing output based on if there are multiple occurrences of an user entered number    
    for num_occurrence in range(len(count)):
        if count[num_occurrence] != 0:
            if count[num_occurrence] == 1:
                print('{} occurs 1 time' .format(num_occurrence))
            else:
                print('{} occurs {} times' .format(num_occurrence,\
                      count[num_occurrence]))

except:
    print('Please enter a valid number')