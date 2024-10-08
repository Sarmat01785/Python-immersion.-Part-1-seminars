"""
Задание №4
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
1. расширение
2. Минимальная длина случайно сгенерированного имени, по умолчанию 6
3. Максимальная длина случайно сгенерированного имени, по умолчанию 30
4. Минимальное число случайных байт, записанных в файл, по умолчанию 256
5. Максимальное число случайных байт, записанных в файл, по умолчанию 4096
6. Количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""

import os
import random
import string
from pathlib import Path


def create_files(
    extension,
    min_name_length=6,
    max_name_length=30,
    min_file_size=256,
    max_file_size=4096,
    num_files=42,
):
    """
    Создает файлы с указанным расширением и случайными именами и содержимым.

    :param extension: Расширение создаваемых файлов.
    :param min_name_length: Минимальная длина имени файла, по умолчанию 6.
    :param max_name_length: Максимальная длина имени файла, по умолчанию 30.
    :param min_file_size: Минимальное количество случайных байт в файле, по умолчанию 256.
    :param max_file_size: Максимальное количество случайных байт в файле, по умолчанию 4096.
    :param num_files: Количество создаваемых файлов, по умолчанию 42.
    """

    # Создаем директорию для хранения файлов, если она еще не существует
    # Используем параметры parents и exist_ok для создания родительских директорий и игнорирования ошибки, если директория существует
    directory = Path("files")
    directory.mkdir(parents=True, exist_ok=True)

    # Цикл для создания указанного количества файлов
    for _ in range(num_files):
        # Генерируем случайное имя файла в заданном диапазоне длин
        file_name = "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=random.randint(min_name_length, max_name_length),
            )
        )
        # Создаем полный путь к файлу с учетом директории и расширения
        file_path = directory / f"{file_name}.{extension}"

        # Открываем файл для записи в бинарном режиме
        with open(file_path, "wb") as file:
            # Записываем случайное количество байт в файл
            file.write(os.urandom(random.randint(min_file_size, max_file_size)))

        # Выводим сообщение о создании файла
        print(f"Файл {file_path} создан.")


# Блок кода, который выполняется при запуске скрипта напрямую
if __name__ == "__main__":
    # Вызываем функцию для создания файлов с расширением 'txt'
    create_files("txt")
