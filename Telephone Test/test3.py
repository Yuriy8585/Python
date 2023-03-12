# Write a program to create a function that takes two arguments, name and age, and print their value.
def print_name_and_age(name, age):
    print("Name:", name)
    print("Age:", age)

# example usage:
print_name_and_age("John", 25)




# Create a function in such a way that we can pass any number of arguments to this function, 
# and the function should process them and display each argument’s value.
def process_arguments(*args):
    for arg in args:
        print("Argument value:", arg)
process_arguments("hello", 42, [1, 2, 3], {"name": "Alice", "age": 30})

