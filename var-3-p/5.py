def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1,100_000):
    R = convert(n,9)
    if R[0] == '7':
        R = R.replace('6', '*')
        R = R.replace('3', '6')
        R = R.replace('*', '3')
        R = '34' + R
    else:
        R = '3' + R[1:] + '45'
    if int(R) < 2876:
        ans.append([n])

print(max(ans))

def cc(n):
    s = ''
    while n != 0:
        s = str(n % 9) +  s
        n //= 9
    return s

def f(n):
    s = cc(n)
    if s[0] == '7':
        s = s.replace('6','*').replace('3','6').replace('*','3')
        s = '34' + s
    else:
        s += '45'
        s = '3' + s[1:]
    return int(s,9)

#1 способ
a = []
for i in range(1,100000):
    if f(i) <  2876:
        a.append([-f(i),-i])
a.sort()
print(abs(a[0][1]))