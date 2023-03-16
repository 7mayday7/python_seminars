"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

count_coins = int(input('Количество монет: '))

count_heads = 0
count_tails = 0

for i in range(count_coins):
    coin = int(input())

    if coin == 0:
        count_heads += 1
    else:
        count_tails += 1

if count_heads < count_tails:
    print(count_heads)
else:
    print(count_tails)
