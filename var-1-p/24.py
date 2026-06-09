from re import finditer
with open(r'.\24_4682 (1).txt') as file:
    data = file.readline()

pattern = r'([AE][BCD])+'
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len))//2)
