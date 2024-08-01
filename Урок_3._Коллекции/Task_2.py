'''
Задача 2

Пользователь вводит данные.
Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число
Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
Строку в верхнем регистре, если в строке есть хотя бы одна буква в нижнем регистре
'''

user_input = input("Введите данные: ")

print("Вы ввели:", user_input)

try:
    int_value = int(user_input)
    if int_value > 0:
        print("Целое положительное число:", int_value)
    else:
        print("Введено не положительное целое число:", int_value)
except ValueError:
    try:
        float_value = float(user_input)
        print("Вещественное число:", float_value)
    except ValueError:
        if any(c.isupper() for c in user_input) and any(c.islower() for c in user_input):
            print("Строка с буквами в разных регистрах переведена в верхний регистр:", user_input.upper())
        elif any(c.isupper() for c in user_input):
            print("Строка с заглавными буквами переведена в нижний регистр:", user_input.lower())
        elif any(c.islower() for c in user_input):
            print("Строка с буквами в нижнем регистре переведена в верхний регистр:", user_input.upper())
        else:
            print("Строка без букв:", user_input)