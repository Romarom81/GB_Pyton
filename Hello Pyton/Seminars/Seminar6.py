#  Zip -  обьединение списков
# a = [1, 2, 3]
# b = ['первый', ' второй', ' третий']
# c = zip (a,b)
# print (list(c))
# for x,y in c:
#     print (x,y)


# enumirate
# a = [6, 23, 256, 56, 32, 457]
# c = list(enumerate(a,10))
# for number, el in enumerate (a, 1):
#         print(number, ' - ', el )
# _____________________________________
#  Задача 1. Напишите программу для построения
#   горизонтальных столбчатых диаграмм с помощью символа звёздочки.
#  ВВод : 3 7 1 10 8
# Вывод ***
#       ********
#       *
# sp = [int(i) for i in input ().split()]
# for i in sp:
#     print (i*'*')

# --------------------------------------
# Задача 2.На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк, которые надо будет отсортировать
# Ввод                   Вывод
#  4
#  три                   три
#  четыре                пять
#  пять                  шесть
#  шесть                 четыре

# n = 4
# sp = []
# for i in range (4):
#     sl = input ()
#     sp.append (sl)
# # sp.sort (key= lambda x:len (x))
# # print (sp)
# print (max(sp,key= lambda x: len(x))) # альтернативный вариант

# --------------------------------------
# Задача 3. Дан список чисел. Вывести из него только простые числа.
#  ВВод                    Вывод
# 15 2 3 31                2 3 31

# def prost (i):
#     for j in range (2,i//2+1):
#             if i%j == 0:
#                 return False
#     return True


# sp = [15, 2, 3, 31]
# res = []
# for i in sp:
#     if prost(i)==True:
#         res.append (i)
# print (res)

# res = list (filter (prost, sp)) #  альтернатив вариант через  фильтр
# print (res)

# --------------------------------
# Задача 4. Преобразовать набор списков (используя функцию zip).
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор:
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние:
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# res_sp = list(zip(users, ids, salary))
# print(res_sp)
# res2_sp = list(zip(*res_sp))
# print (res2_sp)
# ___________________________________

#  Задача 5. Обработка текста.
# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст,
# причём число строк заранее неизвестно. Ваша задача – пронумеровать слова в нём, начиная с нуля,
#  а затем вывести только те слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке.
# (В решении задачи поможет функция enumerate())
# Входные данные :                              На выходе :

# Ехал Грека через реку.                      4 - Видит
# Видит Грека в реке рак.                     1 - Грека
# Сунул в реку руку Грека.                    17 - Греку
# Рак за руку Греку цап.                      0 - Ехал
#                                             14 - Рак
#                                             9 - Сунул

# text = ["Ехал", "Грека", "через", "реку",
#         "Видит", "Грека", "в", "реке", "рак",
#         "Сунул", "в", "реку", "руку", "Грека",
#         "Рак", "за", "руку", "Греку", "цап"]
# text = enumerate(text)
# text = list(filter(lambda x: x[1][0].isupper(), text))
# text.sort(key=lambda x: x[1])
# sp = []
# for x, y in text:
#     if y not in sp:
#         print(x, "-", y)
#     sp.append (y)

