import random

# Список доступных вин
wine_list = {
    'легкое и свежее': ['Совиньон Блан', 'Пино Гриджио', 'Рислинг'],
    'сложное и богатое': ['Шардоне', 'Мерло', 'Каберне Совиньон'],
    'мягкое и фруктовое': ['Пино Нуар', 'Зинфандель', 'Гаме'],
    'теплое и солнечное': ['Шираз', 'Гренаш', 'Мурведр'],
}

# Список рекомендуемых вин в зависимости от погоды
weather_wine = {
    'солнечно': wine_list['теплое и солнечное'],
    'облачно': wine_list['сложное и богатое'],
    'дождливо': wine_list['легкое и свежее'],
}

# Список рекомендуемых вин в зависимости от настроения
mood_wine = {
    'радостное': wine_list['теплое и солнечное'],
    'печальное': wine_list['мягкое и фруктовое'],
    'нейтральное': wine_list['сложное и богатое'],
}

# Запрос настроения и погоды
mood = input('Какое у вас настроение? (радостное, печальное, нейтральное): ')
weather = input('Какая погода? (солнечно, облачно, дождливо): ')

# Рекомендуемое вино
recommended_wine = list(set(weather_wine[weather]) & set(mood_wine[mood]))

# Проверка наличия рекомендуемого вина
if len(recommended_wine) > 0:
    print(f'Рекомендуемое вино: {random.choice(recommended_wine)}')
else:
    print('К сожалению, мы не можем подобрать вино под ваше настроение и погоду')

