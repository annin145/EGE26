from re import finditer

with open(r'.\file\24_4602.txt') as file:
    data = file.readline()

vowels = 'EYUIOA'
pattern = fr'([^{vowels}][{vowels}])+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)) // 2)