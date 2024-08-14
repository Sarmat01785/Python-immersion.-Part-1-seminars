"""
Задача 7

Функция получает на вход словарь с названием компании в качестве ключа 
и списком с доходами и расходами (3-10 чисел) в качестве значения.

Вычислите итоговую прибыль или убыток каждой компании. 
Если все компании прибыльные, верните истину, а если хотя бы одна убыточная - ложь.
"""


def calculate_profit(company_data):

    for company, finances in company_data.items():
        # profit = sum(finances[::2]) - sum(finances[1::2])
        profit = sum(finances)

        if profit < 0:
            return False

    return True


# company_data = {"Company A": [10, 5, 15, 10], "Company B": [30, 10, 10, 20]}

company_data = {
    "Рога": [42, -73, 12, 85, -15, 2],
    "Копыта": [45, 25, -100, 22, 1],
    "Хвосты":[-500, 123, 52, 45, 93],
    }

print(calculate_profit(company_data))
