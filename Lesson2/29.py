"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит 
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не 
такими смышлеными. Никто из ребят не смог до 
конца сделать это задание. Они решили так: у кого 
будет меньше ошибок в коде, тот и выиграл спор. За 
помощью товарищи обратились к Вам, студентам.

"""
import random
length_list = int(input('Input length of list: '))
my_list = [random.randint(0,10) for _ in range(length_list)]
print(my_list)
if 0 in my_list:
    print(max(my_list[:my_list.index(0)]))
else: print(max(my_list))
