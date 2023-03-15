# Напишите программу которая удаляет строку из списка
string_to_remove = input('Enter the string to remove: ')
def remove_string_from_list(list_to_remove, string_to_remove):
    list_to_remove.remove(string_to_remove)
    return list_to_remove

print(remove_string_from_list(['a', 'b', 'c'], 'a'))
print(remove_string_from_list(['a', 'b', 'c'], 'd'))
print(remove_string_from_list(['a', 'b', 'c'], 'c'))