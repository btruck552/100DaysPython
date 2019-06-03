# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:14:36 2019

@author: btruck552
"""
import math  
greeting = "Hello"
_name = "General Kenobi."
Greeting = 'There'
_bestLine_ep3 = 'You are a bold one'

print(greeting + " " + Greeting + "\n\t" + _name+ " " + _bestLine_ep3)

print("{} {}\n\t{} {}".format(greeting,Greeting,_name,_bestLine_ep3))

print(f"{greeting} {Greeting}\n\t {_name} {_bestLine_ep3}")

released = 2005
print("Revenge of the Sith was released on May 4, {}.".format(released))

a=3
b=4
c= math.sqrt(a ** 2 + b ** 2)

print(f"Pythagorean Theorum: a^2 + b^2 = c^2, so when a = {a} and b = {b} then c = {c}")


film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())

var = "Variables are mutable"
print(type(var))
var = 3
print(type(var))
var = 3.5
print(type(var))
var = int(var) # If the variable contains a numeric value, it can be converted to an integer type with the int() function.
print(type(var))
print(var)
var = str(var) # The variable can be converted to a string with the str() function regardless of the contents.
print(type(var))
print(var)
var = float(var) # If the variable contains a numeric value, it can be converted to an float type with the float() function.
print(type(var))
print(var)
var = True
print(type(var))