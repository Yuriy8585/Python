"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

import random
def change_grade(grade_list):
    return str(grade_list).replace(str(max(grade_list)), str(min(grade_list)))

amount = int(input('Input amount of grades: '))
grade_list = [random.randint(1,5) for grade in range(amount)]

print(grade_list)
print(change_grade(grade_list))

"""
import random
lenght_mass = int(input())
random_mass = [random.randit(1,5) for _ in range(lenght_mass)]
print(random_mass)
i=0
while i < len(random_mass):
    if random_mass[i] == 4 or random_mass[i] == 5:
        random_mass[i] = 1
    i += 1
print(random_mass)
"""