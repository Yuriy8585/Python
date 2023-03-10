"""
ФУНКЦИИ MAP, FILTER, REDUCE
"""

get_cube = lambda x : x ** 3

print(get_cube(4))

"""
def f(x)
    return x ** 2
print(f(2))

"""


def run_task(task):
	print('Before running the task')
	task()
	print('After running the task')

run_task(lambda : print('Task is complete!')) # передача анонимной функции
important_task = lambda : print('Important task is complete!') 
run_task(important_task) # передача лямбда-функции




def welcome(user_name):
    print('Welcome, ' + user_name + '!')

welcome('Anon') # вызов функции с параметром




def welcome(user_name:str):
    print('Welcome, ' + user_name + '!')

welcome('Anon') # передача строки в функцию
                # пройдет нормально
welcome(42) # а передача числа в функцию
            # вызовет ошибку




def welcome(first_name:str, last_name:str):
    print('Welcome, ' + first_name + ' ' + last_name + '!')

welcome('Anton', 'Chekhov') # передача аргументов в функцию



# Перевод сток в инт
string = '123456479'
string = list(string)
print(string)
string = list(map(int, string))
print(string)
print(sum(string))


# Перевод сток в инт и обратно
string = '123456479'
string = list(string)
print(string)
string = list(map(lambda x: int(x), string))
print(string)
print(sum(string))
new_list = list(string)


# Четные числа и фильтр

string = '123456479'
string = list(string)
print(string)
string = list(map(lambda x: int(x), string))
print(string)
string = list(filter(lambda x: x % 2 == 0, string))
print(string)




# Перевод строки в инт
def is_odd(num: int) -> bool:  # вводим только инт
    if num % 2 == 1:
        return True
    else:
        return False

string = list(filter(is_odd, string))
print(string)


# Перевод строки в инт
string = list(string)
string = [int(x) for x in string if int(x) % 2 == 0]
print(string)



# Перевод строки в инт
def is_odd(lst: list) -> list:
    new_list = [x for x in lst if int (x) % 2 == 0]
    new_list = list(filter(lambda x: int(x) % 2 != 0, lst))
    return new_list



# нумерация списка

string = '123ghkgkhg456479'
string = list(string)
#string = list(map(lambda x: int(x), string))
print(string)
for i, item in enumerate(string, 1):
    print(f'{i}. {item}')
    print(f'{i}')


# нумерация списка
def func(num: int) -> tuple:
    num1 = num**2
    num2 = num - 2
    return num1, num2
power, minus = func(5)
print (power)
print (minus)


# ZIP
string = '123ghkgkhg456479'
list = [i in range (10)]
string = list(string)
#string = list(map(lambda x: int(x), string))
new_list = list(zip(string, list))
print(string)
print(list)
print(new_list)


new_list = []
for i, item in enumerate(string):
    new_list.append((i, item))
print(new_list)