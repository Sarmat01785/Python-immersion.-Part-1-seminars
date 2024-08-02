"""
Задача 5

Создайте в ручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы.
"""

# Вариант 1
my_list = [4, 5, 7, 2, 3, 6, 7, 1, 3]

odd_indices = [index + 1 for index, value in enumerate(my_list) if value % 2 != 0]

print(f'{my_list=}')
print(f'{odd_indices=}')


# Вариант 2
my_list = [4, 5, 7, 2, 3, 6, 7, 1, 3]

odd_indices = []

for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        odd_indices.append(i + 1)

print(f'{my_list=}')
print(f'{odd_indices=}')
