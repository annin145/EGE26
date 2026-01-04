from re import *

with open(r'.\file\24_1874.txt') as file:
    data = file.readline()

pattern = r'(?<=QW).*?(?=QW)'
matches = [match.group() for match in finditer(pattern, data)]

print(matches)
ans_str = max(matches, key=len)
print(ans_str)

# print(data[pos_ans_str - 100:pos_ans_str])
# print()
# print(data[pos_ans_str:pos_ans_str + len(ans_str)])
# print()
# print(data[pos_ans_str + len(ans_str):pos_ans_str + len(ans_str) + 100])