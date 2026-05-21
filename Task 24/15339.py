from re import finditer
with open(r'.\file\24_15339.txt') as file:
    data = file.readline()

# pattern = r'[6789]?([ABC][6789])+[ABC]?'
# matches = [match.group() for match in finditer(pattern,data)]
# print(len(max(matches,key=len))