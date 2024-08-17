"""
Задача 5
Функция принимает на вход три списка одинаковой длины:

1. Имена str.
2. Ставка int.
3. Премия str с указанием процентов вида «10.25%».

Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""

def calculate_bonus(names, rates, bonuses):
    bonus_dict = {}

    for name, rate, bonus in zip(names, rates, bonuses):
        bonus_percentage = float(bonus.strip("%")) / 100

        bonus_amount = rate * bonus_percentage

        bonus_dict[name] = bonus_amount

    return bonus_dict


names_list = ["Иван", "Николай", "Пётр", "Харитон"]
rates_list = [125_000, 96_000, 109_000, 100_000]
bonuses_list = ["10%", "25.5%", "13.3%", "42.73%"]


print(calculate_bonus(names_list, rates_list, bonuses_list))
