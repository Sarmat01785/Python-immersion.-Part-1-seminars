'''
Задание №1

Пользователь вводит строку из четырёх или более целых чисел, разделённых символом "/".
Сформируйте словарь, где: второе и третье число являются ключами.
Первое число является значением для первого ключа.
Четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.
'''
def create_dictionary_from_input():
    input_string = input("Введите четыре или более числа, разделенные символом '/': ")
    numbers = input_string.split('/')
    
    if len(numbers) < 4:
        print("Ошибка: нужно ввести четыре или более числа.")
        return

    numbers = [int(num) for num in numbers]
    
    result_dict = {numbers[1]: numbers[0], numbers[2]: tuple(numbers[3:])}
    
    return result_dict

result = create_dictionary_from_input()
print(result)
