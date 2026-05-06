from re import finditer

with open(r'..\file\24_6757.txt') as file:
    data = file.readline()

pattern = r'(CFE|FCE)*'

matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len))//3)