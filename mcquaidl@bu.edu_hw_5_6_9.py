# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
10/5/18
Homework 5, Question 6.9
Conversions between feet and meters
"""

def footToMeter(foot):
    """
    Converts from feet to meters
    
    Param 1: feet
    """
    calc_foot = foot * 0.305
     
    return calc_foot #Returns the calculation
    
def meterToFoot(meter):
    """
    Converts from meters to feet
    
    Param 1: meters
    """
    calc_meter = meter / 0.305
    
    return calc_meter #Returns the calculation

def displayChart():
    """
    Display a chart of the conversions from feet to meters and meters to feet
    """
    meter = 20
    
    #Priting out the calculations, while specifically having meters 
    #alternate between 4 and 6 increments
    print('Feet \t Meters  |\tMeters \tFeet')
    for feet in range(1, 11):
        print('{:.1f} \t {:.3f} \t | \t{:.1f} \t {:.3f}' .format(feet,\
              footToMeter(feet), meter, meterToFoot(meter)))
        meter += 5
            
if __name__ == "__main__": 
   displayChart() #Call the description function