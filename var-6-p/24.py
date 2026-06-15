from re import finditer
with open(r'.\24_23206 (1).txt') as file:
    data = file.readline()

pattern = r'([02468][13579A-Z])*S{35}([13579A-Z])*'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches, key=len)))
