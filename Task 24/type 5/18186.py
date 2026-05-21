from re import finditer
with open(r'../file/24_18186.txt') as file:
    data = file.readline()

# pattern = r'([BCDFGH][BCDFGH][AE])+'
# matches = [match.group() for match in finditer(pattern,data)]
# print(max(matches,key=len))
# print(len(max(matches, key=len)))
# #####################################################################3
# cnt = 0
# for i in 'BCDFGH':
#     for j in 'BCDFGH':
#         for k in 'AE':
#             if i+j+k in data:
#                 cnt += 1
#
# print(cnt)
# ###################################################################33
# cnt = 0
# for i in range(len(data)-3):
#     num1,num2,num3 = data[i:i+3]
#     if num1 in 'BCDFGH':
#         if num2 in 'BCDFGH':
#             if num3 in 'AE':
#                 cnt += 1
#
# print(cnt)
###############################################
cnt = 0
sogl = 'BCDFGH'
vovel = 'AE'
for i in range(len(data)-3):
    if data[i] in sogl and data[i+1] in sogl and data[i+2] in vovel:
        i += 3
        cnt +=3
    else:
        i += 1

print(cnt)

