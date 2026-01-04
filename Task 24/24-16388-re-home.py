from re import *

with open(r'.\file\24_16388.txt') as file:
    data = file.readline()

pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))
