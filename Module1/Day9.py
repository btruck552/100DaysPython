# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 09:33:01 2019

@author: btruck552
"""

quotes = ["pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad", "It that what you appreciate about me?"]

print(quotes[0])

print(f"{quotes[2]},\n\t{quotes[3]}\n{quotes[4]}")

print(quotes[2:5])

print(quotes[:2])

print(quotes[::-1])

print(quotes[0][::2])

print(quotes[0][::-1])

wayne = "Toughest guy in letterkenny"
print(wayne[::-1])

print("That's a Texas sized 10-4"[0:9:2])

print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])