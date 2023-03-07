"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

first_elem = int(input('Input first elem: '))
step = int(input('Input step: '))  
amount_elem = int(input('Input amount elem: '))
print([elem for elem in range(first_elem, first_elem + step * amount_elem, step)])