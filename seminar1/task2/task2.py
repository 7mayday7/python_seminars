"""
Найдите сумму цифр трехзначного числа.
"""

num = int(input('Введите 3-значное число: '))

digit1 = num % 10
digit2 = num % 100 // 10
digit3 = num // 100

sum_of_num = digit1 + digit2 + digit3

print(f'Сумма цифр в числе {num} = {sum_of_num}')
