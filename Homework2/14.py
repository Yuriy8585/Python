"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N.
"""

n = int(input())
i = 0
while 2 ** i <= n:
    i += 1
print(2 ** i)

"""
n = int(input())
i = 1
while i < n:
    print(i, end=' ')
    i *= 2
"""