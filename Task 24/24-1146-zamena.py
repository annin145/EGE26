with open(r'.\file\24_1146.txt') as file:
    data= file.readline()

for i in 'ABCEF':
    data = data.replace(i, ' ')

data = data.split()
print(len(min(data, key=len)))