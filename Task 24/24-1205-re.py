from re import *

with open(r'.\file\24_1205-perebor.txt') as file:
    data = file.readline()

pattern = r'[^GWP]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))