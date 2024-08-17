"""
Задача 2

Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def get_descending_unicode_codes(text):

    unicode_codes = {ord(char) for char in text}
    sorted_codes = sorted(unicode_codes, reverse=True)
    return sorted_codes


text_input = "Пример строки с разными символами"
print(get_descending_unicode_codes(text_input))
