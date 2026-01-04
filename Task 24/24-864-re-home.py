from re import *

with open(r'.\file\24_864.txt') as file:
    data = file.readline()

pattern = r'[^EYUIOA]+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))