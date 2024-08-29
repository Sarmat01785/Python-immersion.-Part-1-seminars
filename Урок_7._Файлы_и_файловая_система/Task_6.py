"""
Задание №6
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию - отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

import os
import random
import string
from pathlib import Path


def create_files(
    directory,
    extension,
    min_name_length=6,
    max_name_length=30,
    min_file_size=256,
    max_file_size=4096,
    num_files=42,
):
    """
    Создает файлы с указанным расширением в заданной директории с случайными именами и содержимым.

    :param directory: Путь к директории для создания файлов.
    :param extension: Расширение создаваемых файлов.
    :param min_name_length: Минимальная длина имени файла.
    :param max_name_length: Максимальная длина имени файла.
    :param min_file_size: Минимальное количество случайных байт в файле.
    :param max_file_size: Максимальное количество случайных байт в файле.
    :param num_files: Количество создаваемых файлов.
    """
    # Создаем директорию, если она не существует
    Path(directory).mkdir(parents=True, exist_ok=True)

    for _ in range(num_files):
        file_name = "".join(
            random.choices(
                string.ascii_letters + string.digits,
                k=random.randint(min_name_length, max_name_length),
            )
        )
        file_path = Path(directory) / f"{file_name}.{extension}"

        # Убеждаемся, что имя файла уникально
        while file_path.exists():
            file_name = "".join(
                random.choices(
                    string.ascii_letters + string.digits,
                    k=random.randint(min_name_length, max_name_length),
                )
            )
            file_path = Path(directory) / f"{file_name}.{extension}"

        with open(file_path, "wb") as file:
            file.write(os.urandom(random.randint(min_file_size, max_file_size)))

        print(f"Файл {file_path} создан.")


def generate_files_with_extensions(directory, extensions, files_counts):
    """
    Создает файлы с разными расширениями и разным количеством файлов для каждого расширения в указанной директории.

    :param directory: Путь к директории для создания файлов.
    :param extensions: Список строк с расширениями файлов.
    :param files_counts: Список с количеством файлов для каждого расширения.
    """
    for extension, count in zip(extensions, files_counts):
        create_files(directory, extension, num_files=count)


# Пример использования функции
if __name__ == "__main__":
    extensions_to_generate = ["txt", "log", "csv"]
    files_counts_to_generate = [3, 3, 3]
    target_directory = "target_files"

    generate_files_with_extensions(
        target_directory, extensions_to_generate, files_counts_to_generate
    )
