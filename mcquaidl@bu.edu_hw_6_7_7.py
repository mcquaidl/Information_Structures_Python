# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/11/18
Homework 6, Question 7.7
Algebra: 2 x 2 linear equations
"""

class LinearEquations:
    #Initializing the linear equation variables
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    #Accessor methods for the linear equation variables
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c

    def getD(self):
        return self.d

    def getE(self):
        return self.e

    def getF(self):
        return self.f
    
    #Determining if the problem is solvable
    def isSolvable(self):
        if ((a*d) - (b*c)) != 0:
            return True
        else:
            print('The equation has no solution')
    
    #Solving for x
    def getX(self):
        return float(((e*d) - (b*f)) / ((a*d) - (b*c)))
    
    #Solving for y
    def getY(self):
        return float(((a*f) - (e*c)) / ((a*d) - (b*c)))

try:
    #User is prompted to enter inputs for the linear equation
    a = float(input('Please enter a number for a: '))
    b = float(input('Please enter a number for b: '))
    c = float(input('Please enter a number for c: '))
    d = float(input('Please enter a number for d: '))
    e = float(input('Please enter a number for e: '))
    f = float(input('Please enter a number for f: '))
    
    #Fill the class with the user entered inputs above
    LinearEquations_1 = LinearEquations(a, b, c, d, e, f)
    
    #Call the isSolvable function and if true, print output
    if LinearEquations_1.isSolvable():
        print('\nThe value for x is: {:.2f} \nThe value for y is: {:.2f}' \
              .format(LinearEquations_1.getX(), LinearEquations_1.getY()))

except: #Displays if the user tries to input anything other than a number
    print('Something went wrong, please try again')