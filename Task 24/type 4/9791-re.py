from re import finditer

with open(r'..\file\24_9791.txt') as file:
    data = file.readline()

pattern = r'[1-9A-F][0-9A-F]*|0'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))