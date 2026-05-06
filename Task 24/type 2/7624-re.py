from re import finditer

with open(r'..\file\24_7624.txt') as file:
    data = file.readline()

pattern = r'[XYZ]?([^XYZ]+[XYZ]?)+'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))


