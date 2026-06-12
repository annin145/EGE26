def f(start,end,s1,s2):
    if start == 30: s1 =1
    if start == 60: s2 =1
    if start == end: return 1 and 0 < s1+s2 < 2
    if start > end: return 0
    return f(start+1,end,s1,s2)+f(start*2,end,s1,s2)+f(start*3,end,s1,s2)

print(f(10,70,0,0))