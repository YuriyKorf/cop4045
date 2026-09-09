#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:12:33 2026

@author: Yuriy Korf
p3_Yuriy_Korf.py
COP4045 - Homework 1

"""

# Find a duplicates in a string "s" of length "n"
def find_dup_str(s,n): 
    for i in range(len(s) - n + 1):
        obs_str = s[i:i+n]
        
        for j in range(i + n, len(s) - n + 1):
            if obs_str == s[j:j+n]:
                return obs_str
    
    return ""

# Find the largest duplicate in a string "s"
def find_max_dup(s):
    longest = ""
    
    for n in range(1, len(s) + 1):
        duplicate = find_dup_str(s, n)
        
        if duplicate != "":
            longest = duplicate
        else:
            break
    
    return longest

# Main 

# Testing find_dup_str()
# Tested with the string "Youtube is a red color but could be an ube color" with n = 3, and n = 5.
s1 = input("Enter a string: ")
n = int(input("Enter substring length: "))

result1 = find_dup_str(s1, n)
print(result1)

# Testing find_max_dup()
s2 = input("Enter a string: ")

result2 = find_max_dup(s2)
print(result2)

