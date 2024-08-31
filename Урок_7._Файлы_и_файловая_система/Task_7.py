"""
Задание №7
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

# import os
# import shutil

# # Определяем словарь с категориями файлов и соответствующими расширениями
# CATEGORIES = {
#     "Видео": [".mp4", ".avi", ".mov", ".mkv"],
#     "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
#     "Тексты": [".txt", ".doc", ".docx", ".pdf", ".rtf"],
#     "Музыка": [".mp3", ".wav", ".flac", ".aac"],
#     "Архивы": [".zip", ".rar", ".7z", ".tar"],
# }


# def sort_files(directory):
#     """
#     Функция для сортировки файлов в указанной директории по категориям.

#     :param directory: Путь к директории, в которой необходимо выполнить сортировку.
#     """
#     # Проходим по всем файлам в указанной директории
#     for filename in os.listdir(directory):
#         # Определяем путь к файлу
#         filepath = os.path.join(directory, filename)

#         # Пропускаем папки
#         if os.path.isdir(filepath):
#             continue

#         # Определяем расширение файла
#         file_extension = os.path.splitext(filename)[1].lower()

#         # Определяем категорию файла
#         for category, extensions in CATEGORIES.items():
#             if file_extension in extensions:
#                 # Создаем папку для категории, если она не существует
#                 category_dir = os.path.join(directory, category)
#                 os.makedirs(category_dir, exist_ok=True)

#                 # Перемещаем файл в соответствующую категорию
#                 shutil.move(filepath, os.path.join(category_dir, filename))
#                 break
#         else:
#             # Если файл не подходит ни под одну категорию, он остается в исходной папке
#             print(
#                 f"Файл {filename} не был перемещен, так как не соответствует ни одной категории."
#             )


# if __name__ == "__main__":
#     # Задаем директорию для сортировки
#     directory_to_sort = (r"Укажите путь_к_вашей_директории")

#     # Вызываем функцию сортировки
#     sort_files(directory_to_sort)


import os
from pathlib import Path
from shutil import move


def sort_files_by_type(source_directory):
    """
    Сортирует файлы по директориям в зависимости от их расширения.

    :param source_directory: Путь к исходной директории с файлами.
    """
    # Словарь для сопоставления расширений с типами файлов
    file_types = {
        "video": [".mp4", ".avi", ".mov"],
        "images": [".jpg", ".jpeg", ".png", ".gif"],
        "text": [".txt", ".log", ".md"],
    }

    # Создаем целевые директории для каждого типа файлов
    for type_dir in file_types.keys():
        Path(source_directory, type_dir).mkdir(exist_ok=True)

    # Перебираем файлы в исходной директории
    for file in Path(source_directory).iterdir():
        if file.is_file():  # Убедимся, что это файл, а не директория
            # Перемещаем файл в соответствующую директорию на основе его расширения
            file_ext = file.suffix.lower()
            moved = False
            for type_dir, extensions in file_types.items():
                if file_ext in extensions:
                    move(str(file), str(Path(source_directory, type_dir, file.name)))
                    moved = True
                    break
            if not moved:
                print(
                    f"Файл {file.name} не был перемещен, так как его расширение неизвестно."
                )


# Пример использования функции
if __name__ == "__main__":
    sort_files_by_type(r"Укажите путь_к_вашей_директории")
