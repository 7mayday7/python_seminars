"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход
подается только одно слово, которое содержит либо только английские, либо только русские буквы.
"""

word = input('Введите слово: ')

word_letters = list()

list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list6 = ['J', 'X', 'Ш', 'Э', 'Ю']
list7 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']


score = 0

for i in range(len(word)):
    word_letters.append(word[i])

for i in word:
    if i.upper() in list1:
        score += 1
    elif i.upper() in list2:
        score += 2
    elif i.upper() in list3:
        score += 3
    elif i.upper() in list4:
        score += 4
    elif i.upper() in list5:
        score += 5
    elif i.upper() in list6:
        score += 8
    elif i.upper() in list7:
        score += 10

print(f'Количество очков: {score}')
