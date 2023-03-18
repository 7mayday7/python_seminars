"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random

number_of_items = int(input('Количество элементов в массиве: '))

mas = []
for i in range(number_of_items):
    mas.append(random.randint(1, 5))
print(mas)

number = int(input('Число для подсчета: '))

count = 0

for i in mas:
    if i == number:
        count += 1

print(f'Количество повторений числа {number} → {count}')
