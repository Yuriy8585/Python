"""
15. Иван Васильевич пришел на рынок и решил 
купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз 
потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9

"""

import random
number_watermelon = int(input('Input number of watermelon: '))
weight_1 = random.randint(1, 100)
print(f'Weight of 1 watermelo: {weight_1}')
max_weight = weight_1
min_weight = weight_1
for i in range(number_watermelon - 1):
    weight = random.randomint(1, 100)
    print(f'Weight of {i + 2} watermelon {weight}')
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
print(f'Min weight =  {min_weight}, Max weight = {max_weight}')