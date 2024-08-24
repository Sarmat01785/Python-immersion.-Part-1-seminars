"""
Задание №2
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
Функция выводит подсказки "больше" и "меньше".
Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""

# import random

# def guess_the_number(lower_bound, upper_bound, attempts):
#     """
#     Функция для игры в угадывание случайного числа.

#     Аргументы:
#     lower_bound (int): Нижняя граница диапазона чисел.
#     upper_bound (int): Верхняя граница диапазона чисел.
#     attempts (int): Количество попыток угадать число.

#     Возвращает:
#     bool: Возвращает True, если число угадано, иначе False.
#     """
#     # Генерируем случайное число в заданных границах
#     secret_number = random.randint(lower_bound, upper_bound)

#     # Даем пользователю несколько попыток на угадывание числа
#     for _ in range(attempts):
#         try:
#             # Просим пользователя ввести предполагаемое число
#             guess = int(input(f"Угадайте число между {lower_bound} и {upper_bound}: "))

#             # Проверяем, угадал ли пользователь число
#             if guess == secret_number:
#                 print("Поздравляем! Вы угадали число!")
#                 return True
#             elif guess < secret_number:
#                 print("Больше.")
#             else:
#                 print("Меньше.")
#         except ValueError:
#             print("Пожалуйста, введите целое число.")

#     # Если попытки исчерпаны, возвращаем False
#     print(f"Вы исчерпали попытки. Загаданное число было: {secret_number}")
#     return False

# if __name__ == "__main__":
#     guess_the_number(1, 10, 3)


"""
Задание №3
Улучшаем задачу 2.
Добавьте возможность запуска функции "угадайки" из
модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""

# guess_number.py
import random
import sys


__all__ = ["guess_the_number"]


def guess_the_number(lower_bound=1, upper_bound=100, attempts=5):
    """
    Игра "Угадай число". Загадывается число в заданном диапазоне,
    и пользователь пытается его угадать за ограниченное количество попыток.

    :param lower_bound: Нижняя граница диапазона чисел.
    :param upper_bound: Верхняя граница диапазона чисел.
    :param attempts: Количество попыток для угадывания числа.
    :return: True, если число угадано, иначе False.
    """
    secret_number = random.randint(lower_bound, upper_bound)
    print(f"Угадайте число между {lower_bound} и {upper_bound} за {attempts} попыток.")

    for attempt in range(attempts):
        try:
            guess = int(input(f"Попытка {attempt + 1}. Введите ваше число: "))
            if guess == secret_number:
                print("Поздравляем! Вы угадали число!")
                return True
            elif guess < secret_number:
                print("Больше.")
            else:
                print("Меньше.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"Вы исчерпали все попытки. Загаданное число было: {secret_number}")
    return False


if __name__ == "__main__":
    # Проверяем количество переданных аргументов
    if 1 <= len(sys.argv[1:]) <= 3:
        # Используем генераторное выражение для преобразования аргументов командной строки в числа
        params = [int(arg) for arg in sys.argv[1:]]

        # Распаковываем параметры и вызываем функцию
        guess_the_number(*params)
    else:
        print("Usage: python guess_number.py <lower_bound> <upper_bound> <attempts>")
        print(
            "lower_bound - Нижняя граница диапазона (необязательный параметр, по умолчанию 1)"
        )
        print(
            "upper_bound - Верхняя граница диапазона (необязательный параметр, по умолчанию 100)"
        )
        print("attempts - Количество попыток (необязательный параметр, по умолчанию 5)")
