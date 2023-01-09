# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# str  = ' абвпр рптл  абвлпо  пдпоаи абврмн  '
# str = str.split()
# str2 = list(filter(lambda x: "абв" not in x, str))
# print (str2)

# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# n = int (input(' введите число '))
# hod = 0
# poz = {0: input(' Введите имя первого игрока '),1: input(' введите имя второго игрока ')}
# while n > 0:
#     if n <= 28:
#         print(f' Выиграл игрок - {poz[hod]}')
#         break
#     print(f' ход игрока - {poz[hod]}' )
#     d = int(input(' Сколько конфет берёте?'))
#     while not  1 <= d <= 28:
#         d = int(input(' укажите, сколько конфет вы берёте?'))
#     n -= d
#     print(f' Осталось конфет {n}')
#     hod = (hod+1) % 2

#  Задача 3.Создайте программу для игры в ""Крестики-нолики"".
# pole = range(1, 10)

# def draw_pole(pole):
#     print("-------------")
#     for i in range(3):
#         print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
#         print("-------------")

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input( f"Куда поставим {player_token}? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(pole[player_answer-1]) not in "XO"):
#                 pole[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(pole):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if pole[each[0]] == pole[each[1]] == pole[each[2]]:
#             return pole[each[0]]
#     return False

# def main(pole):
#     counter = 0
#     win = False
#     while not win:
#         draw_pole(pole)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(pole)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_pole(pole)

# main (pole)


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# with open('file_encode.txt', 'w') as data:
#     data.write(
#         'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()


# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(
#     f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')
