from re import *
with open(r'.\file\24_1866-perebor.txt') as file:
    data = file.readline()

pattern = r'(?<=(ad|da)).+?(?=(ad|da))'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))