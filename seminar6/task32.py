"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

list_num = list()

length_list = int(input('Длина списка: '))

for i in range(length_list):
    list_num.append(random.randint(1, 10))

print(f'Список: {list_num}')

min_elem = int(input('\nМинимум: '))
max_elem = int(input('Максимум: '))

for j in range(length_list):
    if min_elem <= list_num[j] <= max_elem:
        print(j)
