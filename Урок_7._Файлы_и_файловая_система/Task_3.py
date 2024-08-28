"""
Задание №3
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
При достижении конца более короткого файла,
возвращайтесь в его начало.
"""

import itertools


def process_files_and_multiply(numbers_file, names_file, result_file):
    """
    Функция считывает числа из файла numbers_file и имена из файла names_file,
    перемножает числа, преобразует имена в зависимости от знака результата
    и записывает их в файл result_file.

    :param numbers_file: Имя файла с парами чисел.
    :param names_file: Имя файла с именами.
    :param result_file: Имя файла для записи результатов.
    """
    # Открываем файлы с числами и именами для чтения
    with open(numbers_file, "r", encoding="utf-8") as num_file, open(
        names_file, "r", encoding="utf-8"
    ) as name_file:
        # Считываем содержимое файлов в списки
        number_lines = num_file.readlines()
        name_lines = name_file.readlines()

    # Открываем файл для записи результатов
    with open(result_file, "w", encoding="utf-8") as result_file:
        # Используем itertools.cycle для циклического прохода по короткому списку
        for name, numbers in zip(itertools.cycle(name_lines), number_lines):
            # Извлекаем числа из строки, преобразуем их в float и int
            int_number, float_number = map(float, numbers.split("|"))
            # Перемножаем числа
            product = int_number * float_number

            # Формируем имя в зависимости от знака результата умножения
            result_name = name.strip().lower() if product < 0 else name.strip().upper()
            # Округляем произведение до целого, если оно положительное, и берем модуль, если отрицательное
            result_product = abs(int(product)) if product < 0 else round(product)

            # Записываем имя и произведение в файл
            result_file.write(f"{result_name}|{result_product}\n")


if __name__ == "__main__":
    process_files_and_multiply(
        "random_numbers.txt", "pseudonyms.txt", "results.txt"
    )  # Пример использования функции
