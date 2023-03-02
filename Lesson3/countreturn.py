import random

list = [random.randint(1, 9) for _ in range(10)]

print(list)
dict = {}
for i in list:
    dict[i] = dict.get(i, -1) + 1
    print(i if dict.get(i) == 0 else f'{i}_{dict.get(i)}', end = ', ')