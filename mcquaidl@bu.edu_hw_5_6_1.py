# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/2/18
Homework 5, Question 6.1
Math: pentagonal numbers
"""

def getPentagonalNumber(n):
    """
    Returns a pentagonal Number
    """
    pentagonal_number = (n*(3*n - 1))/2 #Calculate the pentagonal number       
    
    return int(pentagonal_number) #return the pentagonal number

def printPentagonalNumbers(numberOfPentagonalNumbers):
    """
    Iterates through the numbers to display 10 numbers per line
    
    param 1 - 100 = number fed from the numberOfPentagonalNumbers function
    """
    NUMBER_OF_PENTAGONAL_NUMBERS_PER_LINE = 10 #Display 10 per line
    count = 0 #Count the number of pentagonal numbers
    number = 1 #Number to start the count
    
    #Repeadetedly find pentagonal numbers
    while count < numberOfPentagonalNumbers:
        #Print the pentagonal number and increase the count
        print('{} ' .format(getPentagonalNumber(number)), end="")
        count += 1 #Increase count
        number +=1 #Increase number
        
        if count % NUMBER_OF_PENTAGONAL_NUMBERS_PER_LINE == 0:
            #Print the number and advance to the new line
            print()

def description():
    print('The first 100 pentagonal numbers are: ')
    printPentagonalNumbers(100)


if __name__ == "__main__": 
   description() #Call the description function