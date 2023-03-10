"""
Напишите функцию, которая принимает номер телефона и возвращает его название и имя.
"""
def get_name_and_number(phone_number):
    return f'{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
print(get_name_and_number('+7-888-888-8888'))

def get_phone_name(phone_number):
    return f'Телефон {phone_number}'

print(get_phone_name('+7123456789'))