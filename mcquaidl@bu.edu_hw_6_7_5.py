# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/11/18
Homework 6, Question 7.5
Geometry: n-sided regular polygon 
"""

import math

class RegularPolygon:
    #Initializing the polygon values
    def __init__(self, number=3, side=1.0, x_coordinate=0.0, y_coordinate=0.0):
        self.n = number
        self.side = side
        self.x = x_coordinate
        self.y = y_coordinate
    
    #Mutator method for n, side, x, & y coordinates (redundant?)
    def setN(self, number):
        self.n = number
    
    def setSide(self, side):
        self.side = side
        
    def setX(self, x_coordinate):
        self.x = x_coordinate
        
    def setY(self, y_coordinate):
        self.y = y_coordinate
        
    #Accessor method for n, side, x, & y coordinates
    def getN(self):
        return self.n
        
    def getSide(self):
        return self.side
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    #getPerimeter method which returns the perimeter of the polygon
    def getPerimeter(self):
        return self.n*self.side
    
    #getArea method which returns the area of the polygon
    def getArea(self):
        return (self.n * (self.side**2)) / (4 * math.tan(math.pi/self.n))
    
#Polygon 1 output
polygon_1 = RegularPolygon()
print('The perimeter and area for Polygon 1 is as follows: \nPerimeter: {}\
\nArea: {:.4f}' .format(polygon_1.getPerimeter(), polygon_1.getArea()))

#Polygon 2 output
polygon_2 = RegularPolygon(6,4)
print('\nThe perimeter and area for Polygon 2 is as follows: \nPerimeter:\
{}\nArea: {:.4f}' .format(polygon_2.getPerimeter(), polygon_2.getArea()))

#Polygon 3 output
polygon_3 = RegularPolygon(10, 4, 5.6, 7.8)
print('\nThe perimeter and area for Polygon 3 is as follows: \nPerimeter:\
{}\nArea: {:.4f}' .format(polygon_3.getPerimeter(), polygon_3.getArea()))