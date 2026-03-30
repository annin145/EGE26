with open(r'.\files\17968.txt') as file:
    data = [list(map(int,i.split())) for i in file]

cnt = 0
for line in data:
    max_num = max(line)
    if max_num < sum(line) - max_num:
        ch = [i for i in line if i%2==0]
        not_ch = [i for i in line if i%2 != 0]
        if sum(ch) == sum(not_ch):
            cnt += 1

print(cnt)
