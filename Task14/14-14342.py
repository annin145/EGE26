from string import printable

print(printable[:25])
# 25 <= p <= 36

for p in range(25,37):
    num1 = int('bo', p)
    num2 = int('om', p)
    num3 = int('bl4',p)
    num4 = int('cng', p)
    num = num1 + num2 + num3
    if num == num4:
        print(p)