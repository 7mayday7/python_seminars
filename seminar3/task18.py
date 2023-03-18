"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random

number_of_items = int(input('Количество элементов в массиве: '))

mas = []
for i in range(number_of_items):
    mas.append(random.randint(1, 10))
print(mas)

number = int(input('Число: '))

nearest_element = mas[0]
for i in range(1, number_of_items):
    if abs(mas[i] - number) < abs(nearest_element - number):
        nearest_element = mas[i]

print(f"Ближайший элемент → {nearest_element}")
