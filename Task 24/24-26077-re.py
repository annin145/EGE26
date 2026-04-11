from re import finditer

with open() as file:
    data = file.readline()

pattern = ''
matches = [match.group() for match in finditer([pattern,data])]
print(len(max(data, key=len)))