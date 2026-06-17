from re import finditer
with open(r'.\file\24_17685.txt') as file:
    data = file.readline()

num = r'([1-9][0-9]*|0)'

# 0 * 0 | 17*0 | 0+0 | 17*0+0
# prod1 = fr'{num}\*{num}'
# # prod3 = fr'{num}\*0'
# prod2 = fr'{num}\+{num}'
# prod4 = fr'{num}\+0'
# prod5 = fr'{num}\*{num}\+{num}'

ans = 0
pattern = fr'{num}([+*]{num})+'
matches = [match.group() for match in finditer(pattern,data)]
for match in matches:
    len_match = len(match)
    if eval(match) == 0:
        ans = max(ans,len_match)
    if len_match > ans:
        for l in range(0,len_match-1):
            if match[l] in '+*': continue
            if match[l] == '0' and match[l+1] not in '*+': continue
            for r in range(len_match-1, l, -1):
                if match[r] in '*+': continue
                new_num = match[l:r+1]
                if eval(new_num) == 0:
                    ans = max(ans,len(new_num))
                    break

print(ans)

###################################
# pattern = rf'{num}([+*{num})+'
# pattern = fr'{prod1}[+*]{prod2}'
