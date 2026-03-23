def f(s, base): # функция для перевода списка цифр в число в 10-ичной системе
    s = s[::-1]
    return sum(s[i] * base ** i for i in range(len(s))) # суммируем цифры по разрядам

for x in range(36, -1, -1): # перебираем возможные значения x от максимального к минимальному
    a = [9, 8, x, 3, 1] # первая слагаемая, список цифр
    b = [1, x, 9, 2, 4] # вторая слагаемая, список цифр
    n = f(a, 37) + f(b, 37) # вычисляем сумму этих чисел
    if n % 21 == 0: # если сумма кратна 21
        print(n // 21) # выводим частное
        break # прерываем цикл после первой подходящей (наибольшей) x



def convert(num,sys):
    num = num[::-1]
    res = 0
    for i in range(len(num)):
        res += num[i]*sys**i
    return res

ans = []
for x in range(1,37):
    num1 = convert([9,8,x,3,1], 37)
    num2 = convert([1,x,9,2,4], 37)
    num = num1 + num2
    if num%21== 0:
        ans.append([x,num//21])

print(max(ans))