num = 15
print(id(num)) #id() - выводим айди переменной в оперативной памяти

# целое число / integer / int
my_int = 145
print(my_int, type(my_int))

# Дробные числа / вещественные числа / числа с плавающей точкой / float
my_float = 13.3
print(my_float, type(my_float))

# строки / string / str
my_str_1 = 'hello"'
my_str_2 = "hello'"
print(my_str_1, type(my_str_1))
print(my_str_2, type(my_str_2))

# списки / list
my_list = [13, 63, 'hello', 0.17]
print(my_list, type(my_list))

# кортеж / tuple
my_tuple = ('hello', 'hi', 41)
print(my_tuple, type(my_tuple))

# множество / set
my_set = {1, 2, 3, 2, 1, 3, 1, 2, 3, 1}
print(my_set, type(my_set))

# словарь / dictionary / dict
my_dict = {'name': 'Larisa', 'age':91, 'last name': 'Nesterova'}
print(my_dict, type(my_dict))

# логический тип данных / boolean / bool
my_bool1 = True
my_bool2 = False
print(my_bool1, type(my_bool1))