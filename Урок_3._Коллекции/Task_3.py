'''
Задача 3

Создайте в ручную список с повторяющимися элементами.
Удалите из него все элементы которые встречаются дважды.
'''

my_list = [42, 73, 5, 42, 2, 3, 5, 7, 73, 42]

counts = {}
for item in my_list:
    counts[item] = counts.get(item, 0) + 1

new_list = [item for item in my_list if counts[item] != 2]

print(f'{counts=}')
print(f'{my_list=}')
print(f'{new_list=}')