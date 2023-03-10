
path_to_r = 'File/file.txt'
path_to_w = 'File/file_copy.txt'
path_to_a = 'File/file_append.txt'

with open(path_to_r, 'r', encoding = 'UTF-8') as file:
    data = file.readlines()
print(data)
"""    
with open(path, 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)

with open(path, 'r', encoding = 'utf-8') as file:
    data = file.readline()
    print(data)



with open(path, 'r', encoding = 'utf-8') as file:
    data = file.read()
    print(data)
    
with open(path, 'r', encoding = 'utf-8') as file:
    data = file.readline()
"""
with open(path_to_w, 'w', encoding = 'utf-8') as file:  # запись в файл
    file.write('Hello world!')

with open(path_to_a, 'a', encoding='utf-8') as file:  # добавление в файл
    file.write('\nHello world! was upp!!!')

