with open(r'.\24_23381.txt') as file:
    data = file.readline()

for i in data:
    if i in '02468':
        data= data.replace(i,'0')
    else:
        data = data.replace(i,'1')

for l in range(len(data)):
    