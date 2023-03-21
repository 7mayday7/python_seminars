"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""
import string

list_1 = list()
list_2 = list()

count_elem_1 = int(input('Кол-во элементов первого множества: '))
print('Введите элементы первого множества: ')

for _ in range(count_elem_1):
    list_1.append(int(input()))

count_elem_2 = int(input('\nКол-во элементов второго множества: '))
print('Введите элементы второго множества: ')

for _ in range(count_elem_2):
    list_2.append(int(input()))

print(f'\nПервое множество: {list_1}')
print(f'Второе множество: {list_2}')

set_1 = set(list_1)
set_2 = set(list_2)

result_set = set_1.intersection(set_2)

result_list = list(result_set)
result_list.sort()

print(f'\nРезультат пересечения: {result_list}')
