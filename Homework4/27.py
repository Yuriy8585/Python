"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random
amount_bush = int(input('Input amount of bush: '))
max_sum = 0
garden_list = [random.randint(1,10) for _ in range(amount_bush)]
print(f'Garden/bush: {garden_list}')
for number_bush in range(amount_bush): 
    if number_bush == 1:
        max_berries = garden_list[-1] + sum(garden_list[:2]) 
    elif number_bush == amount_bush:
        max_berries = sum(garden_list[amount_bush-2:]) + garden_list[0]
    else:
        max_berries = sum(garden_list[number_bush-2:number_bush+1])
    if max_berries > max_sum:
        max_sum = max_berries
print(f'Max of berries: {max_sum}')