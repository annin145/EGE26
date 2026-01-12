from re import *

with open(r'..\files\24_1146.txt') as file:
    data= file.readline()

pattern = r'D+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(min(matches, key=len)))