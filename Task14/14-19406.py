# def convert (num,sys):
#     res = ''
#     while num != 0:
#         res += str(num%sys)
#         num //= sys
#     return res [::-1]

from string import printable
def most_num(data):
    most = []
    for i in data:
        most.append([data.count(i), i])
    return int(max(most)[1])

for x in printable[1:35]:
    num1 = int(f'6{x}qr{x}', 35)
    num2 = int(f'{x}59sh', 35)
    num3 = int(f'ph{x}69yw', 35)
    num = num1 + num2 + num3
    if num % most_num(str(num)) == 0:
        print(num // most_num(str(num)))