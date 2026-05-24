from re import finditer
with open(r'.\24_26551.txt') as file:
    data = file.readline()

pattern = r'([1-9ABCD])+([0-9ABCD])*[246AC]'
matches = [match.group() for match in finditer(pattern,data)]
# print(matches)
print(len(max(matches, key=lambda x: int(x,14))))
