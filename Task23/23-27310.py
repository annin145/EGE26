def f(start, end, flag):
    if start in [30, 42]: flag = True
    if start == end and flag: return 1
    if start < end: return 0
    return f(start - 3, end, flag) + f(start - 4, end, flag) + f(start // 2, end, flag)

print(f(78, 2, False))