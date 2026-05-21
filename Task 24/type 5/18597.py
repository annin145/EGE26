from re import finditer

with open(r'..\file\24_18597.txt') as file:
    data = file.readline()
# num_int = r'[1-9][0-9]{3}'
# pattern = fr'({num_int}*(\.{num_int})*[&])*{num_int}+'
# matches = [match.group() for match in finditer(pattern,data)]
# print(len(max(matches,key=len)))
# data = '*****.********* & ***************.******** &'
ans = 0
data = data.split('&')
for line1,line2 in zip(data, data[1:]):
    if '.' not in line1 or '.' not in line2:
        continue
    pos_dot_2_1 = line1.find('.')
    if len(line2[:pos_dot_2_1]) != 4 or line2[0] == '0':
        continue
    pos_dot_2_2 = line2.find('.', pos_dot_2_1 + 1)
    if pos_dot_2_2 == -1 and line2[-1] == '.':
        continue
    if pos_dot_2_2 != -1:
        line2 = line2[:pos_dot_2_2]
        if line2[-1] == '.':
            continue

    pos_dot_1 = line1.rfind('.')
    if pos_dot_1 < 4 or pos_dot_1 == len(line1)-1:
        continue
    line1 = line1[pos_dot_1 - 4:]
    if '.' in line1[:4] or line1[0] == '0':
        continue
    ans = max(ans,len(line1)+len(line2)+1)

print(ans)


