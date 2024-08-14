'''
Задание 6

Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
'''

def sum_between_indices(numbers, start_index, end_index):

    start_index = max(0, start_index)
    end_index = min(len(numbers) - 1, end_index)

    if start_index > end_index:
        start_index, end_index = end_index, start_index

    return sum(numbers[start_index:end_index + 1])

numbers_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

start_index = int(input("Введите начальный индекс: "))
end_index = int(input("Введите конечный индекс: "))

total_sum = sum_between_indices(numbers_list, start_index, end_index)
print(f"Сумма чисел между индексами {start_index} и {end_index} равна: {total_sum}")
