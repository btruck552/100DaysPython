# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:22:40 2019

@author: btruck552
"""

print(range(10))
print(list(range(10)))
print(range(0,9,2) == range(0,10,2))

even = range(0,10,2)
odd = range(1,10,2)

print("The even range is {} and the values are {}".format(even,list(even)))
print("The odd range is {} and the values are {}".format(odd,list(odd)))

even = range(10,0,-2)
odd = range(9,0,-2)
print("The even range is {} and the values are {}".format(even,list(even)))
print("The odd range is {} and the values are {}".format(odd,list(odd)))

val = int(input("Please provide a whole number for divisibility check: "))
request = int(input("Please provide a whole number, less than 1m, to be tested for divisibility: "))

in_range = range(val, 1000000, val) 

if request > 1000000:
   print("Please select a lower number and try again.")
elif request in in_range:
    print("{} is divisible by {}.".format(request, val))
else:
    print("{} is not divisible by {}.".format(request,val))
    
    