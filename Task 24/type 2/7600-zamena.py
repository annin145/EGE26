with open(r'..\file\24_7600.txt') as file:
    data = file.readline()

data = data.replace('QR', 'Q R')
data = data.replace('QS', 'Q S')
data = data.replace('SQ', 'S Q')
data = data.replace('SR', 'S R')
data = data.replace('RS', 'R S')
data = data.replace('RQ', 'R Q')
data = data.replace('QQ', 'Q Q')
data = data.replace('RR', 'R R')
data = data.replace('SS', 'S S')

data = data.split()
print(max(data,key=len))
print(len(max(data, key=len)))