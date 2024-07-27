"""
Задача 4
Напишите программу,которая вычисляет площадь круга и длину окружности по введённому диаметру.

1. Диаметр не превышает 1000 условных единиц
2. Точность вычислений должна составлять не менее 42 знака после запятой.
"""

from decimal import Decimal, InvalidOperation, getcontext

# Установим точность вычислений до 42 знаков после запятой
getcontext().prec = 42

# Константа пи с необходимой точностью
PI = Decimal('3.141592653589793238462643383279502884197')

def calculate_circle(diameter: Decimal) -> tuple[Decimal, Decimal]:
    """
    Вычисляет площадь круга и длину окружности по заданному диаметру.
    
    :param diameter: Диаметр круга.
    :return: Кортеж, содержащий площадь круга и длину окружности.
    """
    radius = diameter / 2
    circle_area = PI * radius ** 2
    circumference = PI * diameter
    return circle_area, circumference

# Запрос диаметра от пользователя
while True:
    try:
        diameter_input = input("Введите диаметр круга (не более 1000 условных единиц): ")
        diameter = Decimal(diameter_input)
        if diameter > 0 and diameter <= 1000:
            break
        elif diameter <= 0:
            print("Диаметр должен быть положительным и не равняться нулю.")
        else:
            print("Диаметр превышает допустимый предел.")
    except InvalidOperation:
        print("Неверный ввод. Введите числовое значение.")

# Вычисляем площадь круга и длину окружности
area, length = calculate_circle(diameter)
print(f"Площадь круга: {area}")
print(f"Длина окружности: {length}")
