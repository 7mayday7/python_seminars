"""
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

first_elem = int(input('Первый элемент: '))
difference = int(input('Разность: '))
count = int(input('Количество: '))

list_progress = list()

for el in range(count):
    list_progress.append(first_elem + el * difference)

print(f'Элементы арифметической прогрессии: {list_progress}')
