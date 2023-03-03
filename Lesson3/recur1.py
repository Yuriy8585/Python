"""
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""
fib1 = int(input('введите порядковый номер фибоначи '))
def fib(fib1):
    if fib1 in [1, 2]:
        return 1
    return fib(fib1 - 1) + fib(fib1 - 2) 
print(fib(fib1))