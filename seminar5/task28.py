"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def sum_num(num_1, num_2):
    if num_1 == 0:
        return num_2
    return sum_num(num_1-1, num_2+1)


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(f'{number1} + {number2} = {sum_num(number1, number2)}')
