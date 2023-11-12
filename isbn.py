#!/usr/bin/python
''' This module checks the ISBN'''
import re
string = input("Enter data to aggregate ") or '''
ISBN 123-4-567-12345-1
ISBN 12-4-567-12345-1
ISBN 123-4-567-12345-
hello world
ISBN 123-4-507-12345-1
ISBN123-4-507-12345-1
'''
pattern = r'ISBN \d{3}-\d{1}-\d{3}-\d{5}-\d{1}'
matches = re.findall(pattern, string)
print (matches)