#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:08:38 2026

@author: Yuriy Korf
p1_Yuriy_Korf.py
COP4045 - Homework 1


"""

from matplotlib import pyplot as plt
import numpy as np


while True:
    a = (input("If you would like to end this program, hit the 'Enter' key. Otherwise, enter the value for a: "))
    if a == "":
        print("Program ended. Thank you!")
        break
    a = float(a)
    b = float(input("Please enter the value for b: "))
    c = float(input("Please enter the value for c: "))
    
    discriminant = (b**2) - (4*a*c)
    axis_of_symmetry = (-1*b)/(2*a)
    root_1 = (-b - (discriminant**(1/2)))/(2*a)
    root_2 = (-b + (discriminant**(1/2)))/(2*a)
    
    if discriminant < 0:
        print("No real solutions")
        domain_interval_start = axis_of_symmetry - 5
        domain_interval_end = axis_of_symmetry + 5
    elif discriminant == 0:
        print("One solution: x = ", root_1)
        domain_interval_start = axis_of_symmetry - 5
        domain_interval_end = axis_of_symmetry + 5
    elif discriminant > 0: 
        print("Two solutions: x1 = ", root_1, ", x2 = ", root_2)
        domain_interval_start = min(root_1, root_2) - 3
        domain_interval_end = max(root_1, root_2) + 3

        
    x = np.linspace(domain_interval_start, domain_interval_end, 150)
    y = (a * (x**2)) + (b * x) + c

    plt.figure()
    plt.plot(x, y)
    plt.axhline(0, color = 'black')      # x-axis
    plt.axvline(0, color = 'black')      # y-axis
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("{}x^2 + {}x + {}".format(a,b,c))
    plt.grid()
    plt.show()