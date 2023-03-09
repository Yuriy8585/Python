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