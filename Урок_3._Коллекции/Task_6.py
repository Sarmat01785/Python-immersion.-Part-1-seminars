""" Задача 6

Пользователь вводит строку текста. 
Вывести каждое слово с новой строки.
Строки нумеруються начиная с единицы.
Слова выводяться отсортированными согласно кодировке Unicode.
Текст выравниваеться по правому краю так, что бы у самого длинного слова был один пробел между ним и номером строки. """


text_input = input("Введите строку текста: ")

words = text_input.split()

sorted_words = sorted(words)

longest_word_length = max(len(word) for word in sorted_words)

for index, word in enumerate(sorted_words, start=1):
    print(f"{index}. {word.rjust(longest_word_length + 1)}")
