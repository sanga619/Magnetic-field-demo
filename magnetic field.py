# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:16:27 2019

@author: AMIT SINGH

###Abhseik kumar project
where B is in tesla if
• µ0 = 4π × 10−7
is the vacuum permeability,
• N is the number of turns of the field coil,
• I is the current in the wire in amperes,
• a is the radius of the coil in meters, and
• x is the axial distance in meters from the center of the coil.
B = µ0N *a*2*I/2 (a2 + r**2)3/2
,
 """
import math 
µ0 = (4*math.pi) * 10**-7

N=float(input("Enter the number of turns of the field coil? "))
I=float(input(" enter I the current in the wire in amperes? "))
a=float(input("Enter a  the radius of the coil in meters ?" ))
x=float(input("Enter  the axial distance in meters from the center of the coil? "))
# now using the formula above we will get the expected output of our program
B = (µ0*N *a*2*I) / 2 *(a**2 + x**2)**3/2
print("The magnetude field is :",B)

