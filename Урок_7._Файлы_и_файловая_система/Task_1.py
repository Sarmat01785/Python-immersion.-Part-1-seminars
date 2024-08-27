'''
Задание №1
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
'''

import random
from pathlib import Path

def fill_file_with_random_numbers(num_lines: int, file_name: Path):
    """
    Функция заполняет указанный файл случайными парами чисел.
    Первое число - целое (int), второе - вещественное (float), разделены вертикальной чертой.
    Количество строк и имя файла передаются как аргументы функции.
    
    :param num_lines: Количество строк для записи в файл.
    :param file_name: Имя файла для записи.
    """
    with open(file_name, 'a', encoding='UTF-8') as f:
        for _ in range(num_lines):
            int_number = random.randint(-1000, 1000)
            float_number = random.uniform(-1000.0, 1000.0)
            f.write(f'{int_number}|{float_number:.2f}\n')

if __name__ == '__main__':
    fill_file_with_random_numbers(10, Path('random_numbers.txt'))




# import random
# from pathlib import Path

# # Импортируем модуль random для генерации случайных чисел
# # Импортируем модуль pathlib для работы с путями к файлам

# def fill_file_with_random_numbers(num_lines: int, file_name: str):
#     """
#     Функция заполняет указанный файл случайными парами чисел.
#     Первое число - целое (int), второе - вещественное (float), разделены вертикальной чертой.
#     Количество строк и имя файла передаются как аргументы функции.
    
#     :param num_lines: Количество строк для записи в файл.
#     :param file_name: Имя файла для записи.
#     """
#     # Открываем файл в режиме 'a' для добавления данных (append)
#     # Используем кодировку UTF-8 для совместимости с различными системами
#     with open(file_name, 'a', encoding='UTF-8') as f:
#         # Перебираем количество строк, которое нужно записать в файл
#         for _ in range(num_lines):
#             # Генерируем случайное целое число в диапазоне от -1000 до 1000
#             int_number = random.randint(-1000, 1000)
#             # Генерируем случайное вещественное число в диапазоне от -1000.0 до 1000.0
#             float_number = random.uniform(-1000.0, 1000.0)
#             # Форматируем вещественное число до двух знаков после запятой
#             f.write(f'{int_number}|{float_number:.2f}\n')

# if __name__ == '__main__':
#     # Вызываем функцию fill_file_with_random_numbers с параметрами
#     fill_file_with_random_numbers(10, Path('random_numbers.txt'))
#     # Здесь мы создаем файл с именем 'random_numbers.txt' и записываем в него 10 строк со случайными числами