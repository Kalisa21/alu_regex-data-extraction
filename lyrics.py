#!/usr/bin/python3
''' This module checks Lyrics'''
import re
text = "[Verse 1] In the JUngle the mighty jungle the lion sleeps to night    [Verse 2]  In the Jungle the quite jungle the lion sleeps to night. "
pattern = r'\[Verse \d\].+'
results = re.findall(pattern,text)
print(results)