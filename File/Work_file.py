"""
path = ['data/file.txt']

file = open(path, 'r', encoding='utf-8')
data = file.read()
data = file.readline()
data = file.readlines()


"""
my_list = []
my_list.append(data)
print(my_list)
"""
print(data)
# WARNING
file.close()
"""
