# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:32:35 2019

@author: btruck552
"""

content = ["Wayne is the toughest guy in Letterkenny.", list(range(0,101,10)), \
           ("Wayne", "Dan", "Katy", "Daryl"), 10.4]


for i in range(0,len(content)):
    type_name = type(content[i])
    if type_name == tuple:
        print("{}: type is {}.".format(content[i],type_name))
    elif type_name == str:
        print("{} Allegedly".format(content[i]))
    elif type_name == float:
        content[i] *= .8
        print(content[i])
    elif type_name == int:
        content[i] *= .9
        print(content[i])
    elif type_name == list:
        new_list = content[i]
        for j in range(0,len(new_list)):
            if type(new_list[j]) == float:
                new_list[j] *= .8
            elif type(new_list[j]) == int:
                new_list[j] *= .9
        print(content[i])
    else:
        print("{} type error in item {}: {}".format(type_name,i,content[i]))
        break

