'''
Задача 4

Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''

# Вариант 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [8, 6, 7, 5, 3, 0, 9]
sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", f"{sorted_numbers=}")



# Вариант 2
def bubble_sort(numbers):
    n = len(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if numbers[i - 1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                swapped = True
        n -= 1

numbers_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers_list)
print("Отсортированный список:", f"{numbers_list=}")
