#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:01:27 2026

@author: Yuriy Korf
p2_Yuriy_Korf.py
COP4045 - Homework 1

"""

def find_Pythagorean(n):
    array_of_integers = []
    valid_triples = []
    for i in range(1, n+1):
        array_of_integers.append(i)
        
    for a in array_of_integers:
        for b in array_of_integers:
            for c in array_of_integers:
                if a**2 + b**2 == c**2:
                    valid_triples.append((a, b, c))
    return valid_triples


triples_list = find_Pythagorean(int(input("Enter a positive integer:  ")))

print("Valid Pythagorean triples:", triples_list)