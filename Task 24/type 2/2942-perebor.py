with open(r'../file/24_2942.txt') as file:
    data = file.readline()

ans = 0

for i in range(len(data)-1):
    if data[i:i+2] in'AB AC':
        cnt = 1
        for j in range(i+2,len(data)-1, 2):
            if data[j:j+2] in 'AB AC':
                cnt += 1
            else:
                break
        ans = max(ans,cnt)

print(ans)
