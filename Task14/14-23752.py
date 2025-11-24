# 1 способ
from string import printable

def convert(num,sys):
    res = ''
    while num != 0:
        res += printable[num%sys]
        num //= sys
    return res[::-1]

num1 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num_27 = convert(num1, 27)
cnt = 0
for i in num_27:
    if int(i, 27)>9: #or - if i > '9'
        cnt +=1

print(cnt)

#####################################################################
# 2 способ

num1 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561

cnt = 0

while num1:
    if num1 % 27 > 9:
        cnt += 1
    num1 //= 27

print(cnt)
