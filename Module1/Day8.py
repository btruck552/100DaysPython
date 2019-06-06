# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:38:16 2019

@author: btruck552
"""

theme = "East", "Bound", "Down"
print(type(theme))
print(theme)

good = ("Bandit","Frog","Snowman")
print(type(good))
print(good)

print(theme[0])
#theme[0] = "West"

return_trip = "West", theme[1], theme[2]
print(return_trip)

movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reid"))
print(movie)
title, year, director, stars = movie
print("Title: {}\nYear: {}\nDirector: {}".format(title,year,director))
print(type(stars))
print(stars)

movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reid"])
title, year, director, cast = movie_list
print(type(cast))
print(cast)
cast.append("Jackie Gleason")
print(cast)

del movie_list
