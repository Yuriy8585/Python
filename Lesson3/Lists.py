ist_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]

print(list_1[0]) # 7

list_1 = list() # создание пустого списка
for i in range(5): # цикл выполнится 5 раз
 n = int(input()) # пользователь вводит целое число
 list_1.append(n) # сохранение элемента в конец списка
# 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
print(list_1) # [12, 7, -1, 21, 0]

"""
Чтобы узнать количество элементов в списке необходимо использовать функцию 
len(имя_списка):
list_1 = [7, 9, 11, 13, 15, 17]
print(len(list_1)) # 6

"""

list_1 = [12, 7, -1, 21, 0]
for i in list_1:
 print(i) # вывод каждого элемента списка
# 1-я итерация цикла(повторение 1): i = 12
# 2-я итерация цикла(повторение 2): i = 7
# 3-я итерация цикла(повторение 3): i = -1
# 4-я итерация цикла(повторение 4): i = 21
# 5-я итерация цикла(повторение 5): i = 0

"""
 Удаление последнего элемента списка.
Метод pop удаляет последний элемент из списка:
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0 
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]

"""
Удаление конкретного элемента из списка.
Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12 
print(list_1) # [7, -1, 21, 0]

"""

# Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0]


#Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
#давайте научимся изменять наш список
#● Отрицательное число в индексе — счёт с конца списка
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]


"""
Кортеж — это неизменяемый список.
Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо
данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
памяти и работают быстрее, по сравнению со списками
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
"""

"""
Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. В словаре для определения 
элемента используется значение ключа (строка, число).
"""
dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐' 
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type' 
del dictionary['left'] # удаление элемента


"""
Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два множества,
Вы можете совершать над ними любые стандартные операции, например, объединение,
пересечение и разность. Давайте разберем их.
"""
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray') 
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok


"""
Операции со множествами в Python:
"""
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}


#TASK
#Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
#Решение:
#1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
#Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
#Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
#Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]


#Lists
numbers = [1, 2, 3, 4, 5]
numbers[0] # returns the first item 
numbers[1] # returns the second item
numbers[-1] # returns the first item from the end
numbers[-2] # returns the second item from the end 
numbers.append(6) # adds 6 to the end
numbers.insert(0, 6) # adds 6 at index position of 0
numbers.remove(6) # removes 6
numbers.pop() # removes the last item
numbers.clear() # removes all the items
numbers.index(8) # returns the index of first occurrence of 8
numbers.sort() # sorts the list
numbers.reverse() # reverses the list
numbers.copy() # returns a copy of the list 

