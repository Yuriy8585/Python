class Human:
    def __init__(self, name: str, age: int, is_work: bool): # Инициализация полей
        self.name = name
        self.age = age
        self.is_work = is_work

    def __str__(self):
        return f"{self.name} is {self.age} years old" # Возвращает объект в виде строки

    def __repr__(self):
        return f"Human('{self.name}', {self.age})"
    def greetings(self):
        if self.is_work:
            print(f"Привет, {self.name}!")
        else:
            print(f"Привет, {self.name}!")
    def good_bye(self):
        if self.is_work:
            print(f"До свидания, {self.name}!")
        else:
            print(f"До свидания, {self.name}!")

stone = Human('Kirill', 20, True)
print(stone.age)
stone.name = 'Stone'
print(stone.name)
stone.greetings()
stone.good_bye()