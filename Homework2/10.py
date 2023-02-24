"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

import random

number = int(input("Введите количество монеток n: "))

orel = 0
reshka = 0
i = 0
for i in range(number):
    side = random.randint(0,1)
    print(f'side of {i + 1} coin = {side}')
    if side == 1:
        orel += 1 
        print("Orel")
        
    else:
        reshka += 1
        print("Reshka")
if orel > reshka or orel < reshka:
    print(f'Количество попыток с ОРЕЛ = {orel}', f'Количество попыток с РЕШКА = {reshka}')
else:
    print(f'Ничья ОРЕЛ = {orel}', f' РЕШКА = {reshka} Попробуйте ещё раз')