'''
Задача 1

Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруються начиная с единицы.
Слова выводяться отсортированными согласно кодировка Unicode.
Текст выравниваеться по правому краю так, что бы у самого длинного слова 
был один пробел между ним и номером строки.
'''
def print_words_right_aligned(text):

    words = sorted(text.split())
    longest_word_length = max(len(word) for word in words)

    for index, word in enumerate(words, start=1):
        print(f"{index}. {word.rjust(longest_word_length + 1)}")


text_input = "это пример текста с разными словами для демонстрации функции"
print_words_right_aligned(text_input)
