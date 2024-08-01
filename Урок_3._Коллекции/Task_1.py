'''
Задача 1

Вручную создайте список с целыми числами,которые повторяються.Получите новый список,
который содержит уникальные (без повтора ) элементы исходного списка.

Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
'''

# Вариант короткое решение
original_list = [1, 2, 3, 2, 4, 5, 5, 6, 1]

unique_list = list(set(original_list))

print(f'{original_list=}')
print(f'{unique_list=}')



# Вариант длинное решение

original_list = [1, 2, 3, 2, 4, 5, 5, 6, 1]

unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(f'{original_list=}')
print(f'{unique_list=}')


