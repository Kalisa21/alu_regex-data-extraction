#!/usr/bin/python3
''' This module checks Twitter handles'''
import re

string = input("Enter the text to match against ") or '''
#F1S467
@hello
@FFFFFF
.hexcolor
#######
#123456
'''
pattern = r'#\b(.{6})\b'
matches = re.findall(pattern,string)
print(matches)