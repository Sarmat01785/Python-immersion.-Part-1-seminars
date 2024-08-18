'''
Задание №3

Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
'''

text = "Пример текста"

letters_to_codes = {char: ord(char) for char in text}

iterator = iter(letters_to_codes.items())

for _ in range(5):
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
