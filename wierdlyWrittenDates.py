#!/usr/bin/python3
''' This module checks weirdly formatted dates'''
import re


string = input("Enter data to Test") or '''
The dates are 01-Jan-2022 and 31-Dec-2022.
I was born on Jan-19 but then I got re-born on 17-Jan-2004
'''
pattern = r"\b(\d{2})-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-(\d{4})\b"

matches = re.findall(pattern, string)
print(matches)
