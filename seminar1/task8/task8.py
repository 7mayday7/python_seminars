"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""

width = int(input('Введите ширину шоколадки: '))
height = int(input('Введите высоту шоколадки: '))

count = int(input('Введите количество долек, которые нужно отломить: '))

if (width == 1 and count == 1) or (height == 1 and count == 1):
    print('Можно!')
elif (count > width * height) or (count % 2 == 1 and count == 1 or width * height % 2 == 1 and count == 1):
    print('Нельзя!')
else:
    print('Можно!')
