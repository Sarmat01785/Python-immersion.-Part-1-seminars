"""
Задание №5

Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти - слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
Превратите решение в генераторное выражение.
"""
def fizzbuzz_gen(max_number):
    return (
        'FizzBuzz' if number % 3 == 0 and number % 5 == 0 else
        'Fizz' if number % 3 == 0 else
        'Buzz' if number % 5 == 0 else
        number
        for number in range(1, max_number + 1)
    )

print( * fizzbuzz_gen(100), sep='\n')


# def fizzbuzz(max_number):
#     for number in range(1, max_number + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print('FizzBuzz')
#         elif number % 3 == 0:
#             print('Fizz')
#         elif number % 5 == 0:
#             print('Buzz')
#         else:
#             print(number)

# # Вызов функции с максимальным числом 100
# fizzbuzz(100)
