from re import *

with open(r'.\file\24_1273-perebor.txt') as file:
    data = file.readline()

pattern = r'(?<=XYZ).+?(?=XYZ)'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) + 4)