"""
Задание №5
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""

import os
import random
import string
from pathlib import Path

def create_files(extension, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):
    """
    Создает файлы с указанным расширением и случайными именами и содержимым.

    :param extension: Расширение создаваемых файлов.
    :param min_name_length: Минимальная длина имени файла.
    :param max_name_length: Максимальная длина имени файла.
    :param min_file_size: Минимальное количество случайных байт в файле.
    :param max_file_size: Максимальное количество случайных байт в файле.
    :param num_files: Количество создаваемых файлов.
    """
    directory = Path("files")
    directory.mkdir(parents=True, exist_ok=True)  # Создаем директорию, если она не существует
    
    for _ in range(num_files):
        # Генерация имени файла
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(min_name_length, max_name_length)))
        file_path = directory / f"{file_name}.{extension}"  # Полный путь к файлу
        
        with open(file_path, 'wb') as file:
            file.write(os.urandom(random.randint(min_file_size, max_file_size)))  # Случайное содержимое файла
        
        print(f"Файл {file_path} создан.")  # Вывод сообщения о создании файла

def generate_files_with_extensions(extensions, files_counts):
    """
    Создает файлы с разными расширениями и разным количеством файлов для каждого расширения.
    
    :param extensions: Список строк с расширениями файлов.
    :param files_counts: Список с количеством файлов для каждого расширения.
    """
    for extension, count in zip(extensions, files_counts):
        create_files(extension, num_files=count)  # Вызываем функцию создания файлов для каждого расширения

# Пример использования функции
if __name__ == "__main__":
    # Список расширений файлов
    extensions_to_generate = ['txt', 'log', 'csv']
    # Список количеств файлов, соответствующих каждому расширению
    files_counts_to_generate = [10, 5, 8]
    
    # Генерация файлов с указанными расширениями и количествами
    generate_files_with_extensions(extensions_to_generate, files_counts_to_generate)
