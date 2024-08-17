"""
Задача 3

Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""


def create_unicode_dict(numbers_str):

    num1, num2 = map(int, numbers_str.split())

    start = min(num1, num2)
    end = max(num1, num2)

    unicode_dict = {chr(i): i for i in range(start, end + 1)}

    return unicode_dict


numbers_input = "76 67"
print(create_unicode_dict(numbers_input))
