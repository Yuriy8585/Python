"""
Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
"""
import random
list = [random.randint(1, 238) for i in range(10)]
print(list)
for i in list:
    if i == 237:
        break
    
    elif i % 2 == 0:
        print(i)
print('Программа остановлена при вводе 237')


"""
Посчитайте, сколько раз символ встречается в строке.
"""
string = 'Python Software Foundation'
print(string)
string.count('o')
print(string.count('o'))

