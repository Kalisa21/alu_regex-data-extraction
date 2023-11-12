#!/usr/bin/python3
import re

string = input("Enter data to filter ") or '''
The movie is titled Sniper (2017), and it's a great film.
The movie is titled Soccer (2012), I am not sure you will like it.
The movies are Tarzan (2022) and Coach (1998).
Tarzan
'''
pattern = r'\b\w+\s\(\d{4}\)'

matches = re.findall(pattern, string)
print(matches)



