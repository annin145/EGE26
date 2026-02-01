from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num%sys]
        num //= sys
    return res[::-1]

num = 2*729**2014 + 2*243**2016 - 2*81**2018 + 2*27**2020 - 2*9**2022 - 2024
num27 = convert(num,27)
cnt = 0
for i in num27:
    if i in printable[10:27]:
        cnt +=1

print(cnt)