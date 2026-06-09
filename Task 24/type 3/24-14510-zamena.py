from re import sub
with open(r'..\file\24_14510.txt') as file:
    data = file.readline()

data = sub(r'[^AEIOUY]{2}[AEIOUY]', '*',data)
data = data.split('*')
ans = 10*10
for i in range(1, len(data)-498-1):
    line = '***' + '***'.join(data[i:i+499]) + '***'
    ans = min(ans,len(line))
print(ans)



