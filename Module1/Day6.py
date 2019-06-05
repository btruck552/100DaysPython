# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:05:18 2019

@author: btruck552
"""

list_1 = []
list_2 = list()

print("List 1 Type {}\nList 2 Type: {}".format(type(list_1), type(list_2)))

text = 'Luggage Combination'

print(list(text))

luggage = [1, 3, 5, 2, 4]
luggage.sort()
print(luggage)

numbers = [1, 2, 3, 4, 5]
numbers_sorted = numbers
numbers_sorted.sort(reverse = True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

numbers = [1, 2, 3, 4, 5]
numbers_sorted = list(numbers)
numbers_sorted.sort(reverse = True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

odd = [1,3,5]
even = [2,4]
luggage = odd + even
print(sorted(luggage))

odd = [1,3,5]
even = [2,4]
luggage.extend(even)
luggage.sort()
print(luggage)

odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print("Unsorted list: {}".format(luggage))
print("Using the sorted() function: {}".format(sorted(luggage)))
luggage.sort()
print("Using the .sort() method: {}".format(luggage))

lines = []
lines.append("They told me to comb the desert.")
lines.append("YOGURT! I hate Yogurt!")
lines.append("We'll meet again.")
print(lines)

luggage = [1,2,3,4,5]
print(luggage.index(5))

quote = 'YoguRt! I Hate Yogurt! Even with strawberries!'
print(quote.count("r"))

luggage = [1,2,4,5]
luggage.insert(2,9)
print(luggage)

luggage = [1,2,3,3,4,5,6]
luggage.pop()
print(luggage)
luggage.pop(2)
print(luggage)

rng = list(range(0,10))
rng.remove(7)
print(rng)

countdown = [5,4,3,2,1]
countdown.reverse()
print(countdown)

sample = list(range(1,13))
times_12 = [i * 12 for i in sample]
print(times_12)

luggage.clear
print(luggage)

luggage = [2,2,3,4,5]
luggage[0] = 1
print(luggage)