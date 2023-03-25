"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""


def exponentiate(num, deg):
    if deg == 0:
        return 1
    return num * exponentiate(num, deg-1)


number = int(input('Введите число: '))
degree = int(input('Введите степень: '))

print(f'Число {number} в степени {degree} = {exponentiate(number, degree)}')
