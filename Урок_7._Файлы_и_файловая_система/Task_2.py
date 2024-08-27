'''
Задание №2
Напишите функцию, которая генерирует
псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
'''

import string
import random

def generate_name():
    """
    Генерирует псевдоимя, соответствующее заданным критериям.
    Имя начинается с заглавной буквы, содержит от 4 до 7 букв
    и включает хотя бы одну гласную букву.
    
    :return: Строка с сгенерированным именем.
    """
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    name_length = random.randint(3, 6)
    name = [random.choice(vowels + consonants) for _ in range(name_length)]
    if not any(letter in vowels for letter in name):
        name[random.randint(0, name_length - 1)] = random.choice(vowels)
    return random.choice(string.ascii_uppercase) + ''.join(name)

def generate_pseudonyms(count, filename):
    """
    Генерирует заданное количество псевдоимен и записывает их в файл.
    
    :param count: Количество псевдоимен для генерации.
    :param filename: Имя файла для записи псевдоимен.
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        for _ in range(count):
            pseudonym = generate_name()
            outfile.write(pseudonym + '\n')


if __name__ == '__main__':
    generate_pseudonyms(10, 'pseudonyms.txt')



# import string
# import random

# def generate_name():
#     """
#     Генерирует псевдоимя, соответствующее заданным критериям.
#     Имя начинается с заглавной буквы, содержит от 4 до 7 букв
#     и включает хотя бы одну гласную букву.
    
#     :return: Строка с сгенерированным именем.
#     """
#     # Строка со всеми гласными буквами
#     vowels = 'aeiou'
#     # Строка со всеми согласными буквами (исключая гласные)
#     consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
#     # Определяем случайную длину имени: от 3 до 6 букв плюс одна заглавная
#     name_length = random.randint(3, 6)
#     # Генерируем список букв для имени, выбирая из гласных и согласных
#     name = [random.choice(vowels + consonants) for _ in range(name_length)]
#     # Проверяем, есть ли в имени гласная буква
#     if not any(letter in vowels for letter in name):
#         # Если гласной нет, добавляем одну на случайную позицию
#         name[random.randint(0, name_length - 1)] = random.choice(vowels)
#     # Возвращаем имя, начинающееся с заглавной буквы
#     return random.choice(string.ascii_uppercase) + ''.join(name)

# def generate_pseudonyms(count, filename):
#     """
#     Генерирует заданное количество псевдоимен и записывает их в файл.
    
#     :param count: Количество псевдоимен для генерации.
#     :param filename: Имя файла для записи псевдоимен.
#     """
#     with open(filename, 'w', encoding='utf-8') as outfile:
#         # Открываем файл для записи с указанием кодировки utf-8
#         for _ in range(count):
#             # Генерируем количество псевдоимен, равное count
#             pseudonym = generate_name()  # Получаем псевдоимя
#             outfile.write(pseudonym + '\n')  # Записываем имя в файл с новой строки

# # Пример использования функции
# # Генерируем десять псевдоимен и записываем их в файл 'pseudonyms.txt'
# generate_pseudonyms(10, 'pseudonyms.txt')
