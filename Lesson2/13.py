"""
Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за 
прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в 
который среднесуточная температура ежедневно превышала 
0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10

Output: 2

days = int(input('Input number of days: '))
temporary_count = 0
final_count = 0
for i in range(days):
    temperature = int(input(f'Input temperature in {i + 1} day: '))
    if temperature > 0:
        temporary_count += 1    
        if temporary_count > final_count:
            final_count = temporary_count
    else:
        temporary_count = 0
print(f'Thaw duration = {final_count} days')
"""

import random

count_day = int(input("Days count: "))
temp = 0
count = 0
count_max = 0

for i in range(count_day):
    temp += random.randint(-2, 2)
    print(temp, end=", ")
    if temp > 0:
        count += 1
    else:
        print(f'++{count}++')
        count = 0
        
    if count > count_max:
        count_max = count
print(count_max)