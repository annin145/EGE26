from re import *

with open(r'.\file\24_865 (1).txt') as file:
    data = file.readline()

pattern = r'[^CF]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))