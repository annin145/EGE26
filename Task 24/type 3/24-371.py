from re import finditer
with open(r'..\file\24-371.txt') as file:
    data = file.readline()

data = data.split('M')

ans = 0
for i in range(len(data)-112):
    line_1 = data[i] # 1
    line_112 = 'M'.join(data[i:i+112]) + 'M' # 1 -112
    line_113 = data[i+112] # 113
    if '.' not in line_112:
        if '.' in line_1:
            line_1 = line_1[line_1.rfind('.') +1:]
        ans = max(ans, len(line_112) + line_113.find('.') +1)

print(ans)

# pattern = r'([^M\.]*M){112}[^M\.]*\.'
# matches = [match.group() for match in finditer(pattern,data)]
# print(len(max(matches, key=len)))