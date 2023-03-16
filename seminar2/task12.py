"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

number1 = int(input('Первое число: '))
number2 = int(input('Второе число: '))

sum_numbers = number1 + number2
product_numbers = number1 * number2

found_numbers = False

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == sum_numbers and x * y == product_numbers:
            print(f'Загаданные числа: {x} и {y}')
            found_numbers = True
            break
    if found_numbers:
        break

if not found_numbers:
    print('Загаданные числа не были найдены.')

