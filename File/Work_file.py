
path = 'File/file.txt'

file = open(path, 'r', encoding='utf-8')
data = file.read()
#data = file.readline()
#data = file.readlines()
# WARNING
#file.close()
"""
my_list = []
my_list.append(data)
print(my_list)
"""
print(data)



