#!/usr/bin/python3
''' This module checks Twitter handles'''
import re


pattern =r'@.+'

z=input("Enter the Twitter Username\n") or '''
@hello
__junior
.one
'''

matches = re.findall(pattern, z)
print(matches)

