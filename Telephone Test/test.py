"""
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

Выведите все элементы, которые меньше 5.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  # вывод всех элементов которые меньше 5
print(list(filter(lambda x: x < 5, a)))

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].

Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(filter(lambda x: x in b, a)))

"""
Отсортируйте словарь по значению в порядке возрастания и убывания.
"""
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(sorted(a.items(), key=lambda x: (x[1], x[0])))


"""
Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
"""

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)


"""
Треугольник Паскаля
"""
def pascal_triangle(n):
    row = [1]
    y = [0]
    for i in range(n):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        y.append(row)
    return y
print(pascal_triangle(5))

"""
Палиндром
"""

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('racecar'))
print(is_palindrome('noon'))
print(is_palindrome('stars'))


"""
Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
"""
def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)


"""
Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
"""

n = int(input('Введите число: '))
a = []
b = ()
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b += (a[i],)
print(a)
print(b)
print(sorted(b))
print(sorted(b, reverse=True))
print(sorted(b, key=lambda x: x[0]))
print(sorted(b, key=lambda x: x[1]))
print(sorted(b, key=lambda x: x[0], reverse=True))
print(sorted(b, key=lambda x: x[1], reverse=True))

values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)


