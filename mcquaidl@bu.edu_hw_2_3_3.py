# -*- coding: utf-8 -*-
"""
Larry McQuaid
MET CS 521
9/15/18
Homework 2, Question 3.3
Geography: estimate areas
"""

import math

atlanta_latitude = 33.7489954
atlanta_longitude = -84.3879824

orlando_latitude = 28.5383355
orlando_longitude = -81.37923649999999

savannah_latitude = 32.0808989
savannah_longitude = -81.09120300000001

charlotte_latitude = 35.2270869
charlotte_longitude = -80.84312669999997

atlanta_to_orlando = 6371.01 * (math.acos(
        (math.sin(math.radians(atlanta_latitude)))
        * (math.sin(math.radians(orlando_latitude)))
        + (math.cos(math.radians(atlanta_latitude)))
        * (math.cos(math.radians(orlando_latitude)))
        * (math.cos(math.radians(atlanta_longitude - orlando_longitude)))))

orlando_to_savannah = 6371.01 * (math.acos(
        (math.sin(math.radians(orlando_latitude)))
        * (math.sin(math.radians(savannah_latitude)))
        + (math.cos(math.radians(orlando_latitude)))
        * (math.cos(math.radians(savannah_latitude)))
        * (math.cos(math.radians(orlando_longitude - savannah_longitude)))))

savannah_to_atlanta = 6371.01 * (math.acos(
        (math.sin(math.radians(savannah_latitude)))
        * (math.sin(math.radians(atlanta_latitude)))
        + (math.cos(math.radians(savannah_latitude)))
        * (math.cos(math.radians(atlanta_latitude)))
        * (math.cos(math.radians(savannah_longitude - atlanta_longitude)))))

atlanta_to_charlotte = 6371.01 * (math.acos(
        (math.sin(math.radians(atlanta_latitude)))
        * (math.sin(math.radians(charlotte_latitude)))
        + (math.cos(math.radians(atlanta_latitude)))
        * (math.cos(math.radians(charlotte_latitude)))
        * (math.cos(math.radians(atlanta_longitude - charlotte_longitude)))))

charlotte_to_savannah = 6371.01 * (math.acos(
        (math.sin(math.radians(charlotte_latitude)))
        * (math.sin(math.radians(savannah_latitude)))
        + (math.cos(math.radians(charlotte_latitude)))
        * (math.cos(math.radians(savannah_latitude)))
        * (math.cos(math.radians(charlotte_longitude - savannah_longitude)))))
                
        
triangle_1_side_length = ((atlanta_to_orlando
                          + orlando_to_savannah
                          + savannah_to_atlanta)/2)

triangle_1_area = (math.sqrt((triangle_1_side_length
                              * (triangle_1_side_length
                                 - atlanta_to_orlando)
                              * (triangle_1_side_length
                                 - orlando_to_savannah)
                              * (triangle_1_side_length
                                 - savannah_to_atlanta))))
 
triangle_2_side_length = ((atlanta_to_charlotte
                          + charlotte_to_savannah
                          + savannah_to_atlanta)/2)

triangle_2_area = (math.sqrt((triangle_2_side_length
                              * (triangle_2_side_length
                                 - atlanta_to_charlotte)
                              * (triangle_2_side_length
                                 - charlotte_to_savannah)
                              * (triangle_2_side_length
                                 - savannah_to_atlanta))))
                              
total_area_estimate = triangle_1_area + triangle_2_area

print('The estimated area enclosed by these four cities is {} km'\
      .format(total_area_estimate))