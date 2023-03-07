"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random
length_list = int(input('Input length of list: '))
my_range = [int(input(f'Input {i+1} border of range: ')) for i in range(2)] #2 значения начального индекса и конечного
my_list = [i for i in range(length_list)]
index_list = [i for i in range(length_list) if (my_range[0] <= my_list[i] <= my_range[1])]
print(f'My list: {my_list}')
print(f'Index list: {index_list}')

