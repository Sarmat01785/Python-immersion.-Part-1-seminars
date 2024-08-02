"""
Задача 4

Создайте в ручную картеж содержащий элементы разных типов.
Получите из него словарь списков,где: 
Ключ - тип элемента
Значение - список элементов данного типа
"""

# Вариат 1
# my_tuple = (1, "Строка", 3.14, 2, "Другая строка", 5.5, True, "Ещё строка", 42, False)

# type_dict = {}

# for item in my_tuple:
#     item_type = type(item)
#     if item_type not in type_dict:
#         type_dict[item_type] = [item]
#     else:
#         type_dict[item_type].append(item)

# print('\n')
# print(f'{my_tuple=}\n')
# print(f'{type_dict=}')


# # Вариат 2 (более сложный)
my_tuple = (1, "Строка", 3.14, 2, "Другая строка", 5.5, True, "Ещё строка", 42, False)

type_dict = {}

for item in my_tuple:
    item_type = type(item)
    if not isinstance(type_dict.get(item_type), list):
        type_dict[item_type] = []
    type_dict[item_type].append(item)


print('\n')
print(f"{my_tuple=}")
print(f"{type_dict=}")

'''
Функция isinstance() в этом примере используется для проверки, является ли значение, полученное из словаря для данного типа, списком.
Если нет, то создается новый список. Это немного более явный способ проверить существование ключа в словаре и его соответствие списку,
что может быть полезно в более сложных ситуациях, когда типы значений в словаре могут быть разнообразными.
'''
