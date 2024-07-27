'''
Задача 5
1. Напишите программу которая решает квадратные уравнения даже если дискриминант отрицательный.
2. Используйте комплексные числа для извлечения квадратного корня.
'''

import cmath

def solve_quadratic(a: float, b: float, c: float) -> tuple[complex, complex]:
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    :param a: Коэффициент при x^2.
    :param b: Коэффициент при x.
    :param c: Свободный член.
    :return: Кортеж с двумя значениями - корнями уравнения.
    """
    # Вычисляем дискриминант
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Вычисляем два корня уравнения
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    
    return root1, root2

# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Решаем квадратное уравнение
roots = solve_quadratic(a, b, c)
print(f"Корни уравнения: {roots[0]}, {roots[1]}")
