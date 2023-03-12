"""
Напишите функцию, которая принимает номер телефона и возвращает его название и имя.
"""
def get_name_and_number(phone_number):
    return f'{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}'
print(get_name_and_number('+7-888-888-8888'))

def get_phone_name(phone_number):
    return f'Телефон {phone_number}'

print(get_phone_name('+7123456789'))





# Initialize an empty dictionary to store phonebook entries
phonebook = {}

# Function to add a new entry to the phonebook
def add_entry(name, number):
    phonebook[name] = number
    print(f"Added {name} with number {number} to the phonebook")

# Function to look up a number in the phonebook
def lookup_number(name):
    if name in phonebook:
        print(f"The number for {name} is {phonebook[name]}")
    else:
        print(f"{name} is not in the phonebook")

# Example usage
add_entry("Alice", "555-1234")
add_entry("Bob", "555-5678")
lookup_number("Alice")
lookup_number("Charlie")
