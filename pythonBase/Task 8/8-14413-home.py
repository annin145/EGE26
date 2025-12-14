from itertools import permutations


cnt = 0
for val in set(permutations('сортировка')):
    val = ''.join(val)
    for gl in 'иоа':
            val = val.replace(gl, '@')
    for sogl in 'сртвк':
        val = val.replace(sogl, '*')
    if '***' not in val and '@@@' not in val:
        cnt += 1
print(cnt)

#185760