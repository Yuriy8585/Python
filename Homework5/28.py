"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""

num = int(input('input A '))
num2 = int(input("input B "))
zero = 0
def sum(num, num2):
    if num >= 0 and num2 >= 0:
        return sum(num+1, num2-1)
    elif num == 0 and num2 == 0:
        return zero
    else:
        return num+num2


print(f'Результат суммы {num} и  {num2} равен {sum(num, num2)}')