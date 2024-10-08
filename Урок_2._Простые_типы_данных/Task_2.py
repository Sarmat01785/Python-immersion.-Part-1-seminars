"""
Задача 2

Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле вывидите:
1. Порядковый номер начиная с единицы
2. Значение
3. Адрес в памяти
4. Размер памяти
5. Хэш объекта
6. Результат проверки на целое число только если он положительный
7. Результат проверки на строку только если он положительный
Добавьте в список повторяющейся элементы сравните на результаты.
"""

# Вариант 1

import sys

# Создаем список с элементами разных типов данных
data = [123, 3.14, 'Hello', True, [1, 2, 3], (4, 5), {6: 'six', 7: 'seven'}, {8, 9}, None, 123, 'Hello', False]

# Проходим по элементам списка и выводим информацию о каждом элементе
for i, item in enumerate(data, start=1):
    print(f"Порядковый номер: {i}")
    print(f"Значение: {item}")
    print(f"Адрес в памяти: {id(item)}")
    print(f"Размер памяти: {sys.getsizeof(item)}")
    
    try:
        print(f"Хэш объекта: {hash(item)}")
    except TypeError:
        print("Хэш объекта: Невозможно вычислить")
    
    # Проверяем, является ли элемент целым числом
    if isinstance(item, int):
        print("Результат проверки на целое число: Да")
    
    # Проверяем, является ли элемент строкой
    if isinstance(item, str):
        print("Результат проверки на строку: Да")
    
    print('-' * 40)


# Вариант 2

import sys

data = [1, 'string', 1.0, True, None, [1, 2], {'key': 'value'}, (1,)]

for i, value in enumerate(data, start=1):
    print(f"{i}. {value}")
    print(f"\tАдрес в памяти: {id(value)}")
    print(f"\tРазмер памяти: {sys.getsizeof(value)}")
    
    try:
        print(f"\tХэш объекта: {hash(value)}")
    except TypeError:
        print(f"\tХэш объекта: Невозможно вычислить")
    
    # Проверка на целое число
    if isinstance(value, int):
        print(f"\tЦелое число: {value}")
    
    # Проверка на строку
    if isinstance(value, str):
        print(f"\tСтрока: {value}")

