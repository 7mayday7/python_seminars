"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме
последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
"""

num_of_ticket = int(input('Введите 6-значный номер билета: '))

first_half_number = num_of_ticket // 1000
second_half_number = num_of_ticket % 1000

sum_first_half = (num_of_ticket // 100000) + ((num_of_ticket // 10000) % 10) + ((num_of_ticket // 1000) % 10)
sum_second_half = (second_half_number // 100) + ((second_half_number // 10) % 10) + (second_half_number % 10)

if sum_first_half == sum_second_half:
    print('У вас счастливый билет :)')
else:
    print('У вас не счастливый билет :(')

print()
