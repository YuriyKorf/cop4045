#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:41:01 2026

@author: Yuriy Korf
p4_Yuriy_Korf.py
COP4045 - Homework 1

"""
import math
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns): 
   print("- " * 12)
   print("{:>8}{:>8}".format("x", "y"))
   print("- " * 12)
   
   
   (xmin, xmax) = domain
   xs = []
   ys = []
    
   #interval = (xmax - xmin) / (ns - 1)
   
   for i in range(0, ns):
       xs.append(xmin + ((xmax - xmin) / (ns - 1)) * i)
   for x in xs:
       y = eval(fun_str)
       ys.append(y)
       
       print("{0:>+10.4f}{1:>+10.4f}".format(x, y))
   
    
   plt.plot(xs, ys)
   plt.xlabel("x")
   plt.ylabel("y")
   plt.title(fun_str)
   plt.show()
     
    
   
#main   
fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

plot_function(fun_str, (xmin, xmax), ns)

    