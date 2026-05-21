with open(r'../file/24-384.txt') as file:
    data = file.readline()
ans = 100000000000000000000

data = data.replace('Z', 'Z Z').split()

for i in range(len(data)-268):
    line = ''.join(data[i:i+269]).replace('ZZ', 'Z')
    ans = min(ans,len(line))

print(ans)

