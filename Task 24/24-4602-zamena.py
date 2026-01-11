from string import ascii_uppercase

with open(r'.\file\24_4602.txt') as file:
    data = file.readline()

vowels = 'EYUIOA'
for i in ascii_uppercase:
    if i in vowels:
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '#')

data = data.replace('#*', '!')
data = data.replace('*', ' ')
data = data.replace('#', ' ')

data = data.split()
print(len(max(data, key=len)))

