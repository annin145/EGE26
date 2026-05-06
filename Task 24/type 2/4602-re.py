from re import finditer
with open(r'..\file\24_4602.txt') as file:
    data = file.readline()

pattern = r'([BCD][AO])+'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len))//2)