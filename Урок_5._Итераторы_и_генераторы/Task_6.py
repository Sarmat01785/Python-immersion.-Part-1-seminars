"""
Задание №6

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - отдельный пример таблицы умножения.
Для вывода результата используйте «принт» без перехода на новую строку.
"""

multiplication_table = (f"{i} X {j:2} = {i * j:2}" for i in range(2, 10) for j in range(2, 11))

columns1 = [f"{i} X {j:2} = {i * j:2}" for i in range(2, 6) for j in range(2, 11)]
columns2 = [f"{i} X {j:2} = {i * j:2}" for i in range(6, 10) for j in range(2, 11)]

for row in range(9):
    for col in range(4):
        print(columns1[row + col * 9].ljust(15), end="")
    print()

print()

for row in range(9):
    for col in range(4):
        print(columns2[row + col * 9].ljust(15), end="")
    print()



# LOWER_LIMIT = 2
# UPPER_LIMIT = 11
# COLUMNS = 4
# for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS):
#     for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
#         for num_1 in range(row, row + COLUMNS):
#             print(f"{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}", end="\t")
#         print()
#     print()
