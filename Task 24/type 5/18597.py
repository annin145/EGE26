from re import finditer

with open(r'..\file\24_18597.txt') as file:
    data = file.readline()
num = r'([1-9][0-9]*|0)'
pattern = fr'({num}*(\.{num})*[&])*{num}+'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))