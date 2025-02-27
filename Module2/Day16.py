# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:30:29 2019

@author: btruck552
"""

suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
investigators = set(["Dave Kujan", "Jack Baer", "Jeff Rabin"])
print(suspects)
print(investigators)

suspects.add("Hockney")
print(suspects)

for person in suspects:
 	print("{} was brought in for a line up.".format(person))
     
numbers1 = set([1, 2, 3, 4, 5])
numbers2 = set([6, 7, 8, 9, 10])
print(numbers1.union(numbers2))

evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.intersection(evens))

evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.difference(evens))

evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Evens Difference Update: {}".format(nums.difference_update(evens)))
print("Evens: {}".format(nums))

evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.symmetric_difference(evens))

evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("nums: {}".format(nums))
print("Symmetric Difference Update: {}".format(nums.symmetric_difference_update(evens)))
print("nums: {}".format(nums))

print(suspects)
print(sorted(suspects))

evens = set([0, 2, 4, 6, 8])
evens.discard(0)
evens.remove(2)
print(evens)
evens.discard(0)
#evens.remove(2)
print(evens)

suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
try:
   suspects.remove("Kaiser Soze")
except KeyError:
   print("Kaiser Soze is not one of the usual suspects.")
   
suspects = frozenset(["Verbal", "Keaton", "McManus", "Fenster"])
#suspects.add("Kaiser Soze")
print(suspects)

print(nums)
nums.clear()
print(nums)