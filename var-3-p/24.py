from re import finditer

with open(r'.\24_28006.txt') as file:
    data = file.readline()

pattern = r'(\(([2468]|[1-9][0-9]*[02468])[+\-]([13579]|[1-9][0-9]*[13579])\))+'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))