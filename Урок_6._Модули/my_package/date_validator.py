"""
Задание №7
Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
Проверку года на високосность вынести в отдельную
защищённую функцию.
"""

# date_validator.py

__all___ = ["validate_date"]


def _is_leap_year(year):
    """
    Определяет, является ли год високосным.

    :param year: Год, который необходимо проверить.
    :return: True, если год високосный, иначе False.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_date(date_str):
    """
    Проверяет, может ли заданная дата существовать.

    :param date_str: Строка с датой в формате DD.MM.YYYY.
    :return: True, если дата корректная и может существовать, иначе False.
    """
    # Определяем количество дней в месяцах
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        # Разделяем дату на компоненты
        day, month, year = map(int, date_str.split("."))

        # Проверяем корректность года
        if not 1 <= year <= 9999:
            return False

        # Проверяем корректность месяца
        if not 1 <= month <= 12:
            return False

        # Корректируем количество дней в феврале для високосного года
        if _is_leap_year(year):
            days_in_month[1] = 29

        # Проверяем корректность дня
        return 1 <= day <= days_in_month[month - 1]

    except (ValueError, IndexError):
        # Отлавливаем ошибки преобразования и выход за пределы списка
        return False


# Пример использования функции:
if __name__ == "__main__":
    print(validate_date("29.02.2000"))  # Выведет: True
    print(validate_date("29.02.2001"))  # Выведет: False
