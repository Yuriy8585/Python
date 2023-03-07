"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: Вывод:
1 2 3 2 3 2

"""
"""
import random 

lenght = int(input("Введите количество элементов в списке ")) # цикл выполнится 5 раз
list_1 = [random.randint(1, 10) for i in range(lenght)]
print(list_1)
count = 0
for i in list_1:
    if list_1.count(i) > 1:
        count += 1
print(count // 2)

"""

import random 

lenght = int(input("Введите количество элементов в списке ")) # цикл выполнится 5 раз
list_1 = [random.randint(1, 10) for i in range(lenght)]
print(list_1)
count = 0
pairs_list = []
for item in set(list_1):
    pairs = list_1.count(item)//2
    count += pairs
    if pairs:
        [pairs_list.append(item) for _ in range(pairs*2)]
    [list_1.remove(item) for _ in range(pairs*2)]

print(pairs_list)
print(list_1)
print(f'У нас {count} пар элементов')

 