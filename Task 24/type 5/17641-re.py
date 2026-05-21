from re import finditer
with open(r'..\file\24_17641.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'
prod = fr'({num}\*)*0(\*{num})*'
pattern = fr'({prod}\+)+{prod}'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))