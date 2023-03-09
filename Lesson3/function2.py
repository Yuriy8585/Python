"""
Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как
превратить list строк в list чисел?

"""
"""
data = '1 2 3 5 8 15 23 38'.split()     # функция строка.split() - убирает все пробелы и создаем список из значений строки
print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
"""
"""
data = list(map(int,input().split()))
print(data) # [1, 2, 3, 5, 8, 15, 23, 38]
"""


def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

"""
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True.
data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res) # filter() позволит избавиться от функции where
res = list(map(lambda x: (x, x ** 2), res))
print(res)
"""