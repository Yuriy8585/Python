"""
Написать программу, которая состоит 4 из этапов:
- создает список из рандомных четырех значных чисел
- принимает с консоли цифру и удаляет ее из всех элементов списка
- цифры каждого элемента суммирует пока результат не станет однозначным числом
- из финального списка убирает все дублирующиеся элементы
- после каждого этапа выводить результат в консоль
Пример:
- 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
- 2 этап: Введите цифру: 3
- 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
- 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
- 3 этап: [3, 1, 5, 5, 3, 5, 4]
- 4 этап: [3, 1, 5, 4]
"""

list_1 = [2634, 6934, 7286, 3353, 4602, 3176, 3796]
print(list_1)

list_2= []
number = input('input 3')
for value in list_1:
    elem = str(value)
    if number in elem:
        elem = elem.replace(number, '')
    list_2.append(elem)
print(list_2)

list_3= []
for value in list_2:
    while int(value) > 9:
        value = sum(int(elem) for elem in str(value))
        #first_num = value % 10
        #second_num = value % 100 // 10
        #third_num = value // 100
        # print(value, end=' ')
    list_3.append(value)
print(list_3)


list_4 = set(list_3)
print(list_4)