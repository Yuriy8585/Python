# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
length = int(input('Введите количество чисел: '))
my_number = int(input('Введите искомое число: '))
random_mass = [random.randint(1,100) 
for _ in range(length)]
min_delta = max(random_mass)


for index in range(length):
    if abs(my_number - random_mass[index]) < min_delta:
        min_delta = abs(my_number - random_mass[index])
        search_number = random_mass[index]

print(f'Числа: {random_mass}')
print(f'Искомое число = {search_number}')

