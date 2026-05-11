from re import finditer

with open(r'..\file\24_21908.txt') as file:
    data = file.readline()

pattern = r'[1-9A-D][0-9A-D]*[02468AC]'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=lambda x: int(x, 14))))