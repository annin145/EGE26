from re import finditer
with open(r'..\file\24_28943.txt') as file:
    data = file.readline()
ans = []
data = data[::-1]
for i in 'AEIOUY':
    data = data.replace(i, '*')
data = data.split('02')
for i in range(len(data)-24):
    line = '02'.join(data[i:i+26]) + '02'
    if line.count('*') == 1 and line[0] == '*':
        # data[i+25]
        ans.append(line)
print(len(min(ans,key=len)))
###############################################
# data = data.replace('20', '#')
# pattern = r'(#[^AIEOUY#]*){26}[AIEOUY]'
# matches = [match.group() for match in finditer(pattern,data)]
# print(len(min(matches,key=len).replace('#','20')))


