def f(start,end,num):
    if start == end: return 1
    if start > end or start == num : return 0
    return f(start+1,end,num)+f(start+2,end,num)+f(start+4,end,num)+f(start+8,end,num)

ans1 = f(16, 24,32) * f(24, 48,32)
ans2 = f(16, 32,24) * f(32, 48,24)
print(ans1 + ans2)