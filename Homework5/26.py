"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
num = int(input('input A '))
num2 = int(input("input B "))

def check_num(num, num2):
    if num2 >= 1:
        return num**num2
    elif num2 <= -1:
        return num**num2
    else:
        return zero

zero = 1
print(f'Результат возведения {num} в степень {num2} равен 3{check_num(num, num2)}')