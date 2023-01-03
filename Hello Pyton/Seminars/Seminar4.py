#  1.	Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# str = input(' Введите число').split()
# print (str)
# str = [int(i) for i in str]
# print (str)
# print (f"Максимум: {max(str)}")
# print ( f"Минимум: {min(str)}")

# ==========================================================
# 2.	Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#         1.	с помощью математических формул нахождения корней квадратного уравнения
#         2.	с помощью дополнительных библиотек Python
#  1 способ :

# f = "5x^2 + 3x + -7 = 0"
# f = f[:-3]
# print (f)
# f = f.split("+")
# print(f)
# abc = []
# for i in f:
#     abc.append(int(i.split("x")[0]))
# print(abc)
# a,b,c = abc
# dis = b**2 - 4 * a * c
# print (dis)
# if dis>0:
#     x1 = round ((-b - dis**0,5)//(2 * a),2)
#     x2 = round( + (-b - dis**0,5)//(2 * a),2)
#     print (x1,x2)
# elif dis==0:
#     x1 = (-b )//(2 * a)
#     print (x1)
# else:
#     print (" Корней нет")
#  2 Способ:
# import math

# f = "5x^2 + 3x + -7 = 0"
# f = f[:-3]
# print (f)
# f = f.split("+")
# print(f)
# abc = []
# for i in f:
#     abc.append(int(i.split("x")[0]))
# print(abc)
# a,b,c = abc
# dis = b**2 - 4 * a * c
# print (dis)
# if dis>0:
#     x1 = round ((-b - math.sqrt(dis))//(2 * a),2)
#     x2 = round( + (-b - math.sqrt(dis))//(2 * a),2)
#     print (x1,x2)
# elif dis==0:
#     x1 = (-b )//(2 * a)
#     print (x1)
# else:
#     print (" Корней нет")
# =======================================================
#  3. 3.	Задайте два числа.
#  Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a = 10
# b = 15
# if a > b:
#     for i in range (1,b+1):
#         if (a * i )% b == 0:
#             print (a *i)
#             break
# elif a<b:
#     for i in range (1,b+1):
#         if (b * i )% b == 0:
#             print (b * i )
#             break
# else:
#     print(a)
# ========================================================
# 4. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
#   слова разделены одним или большим числом пробелов или символами конца строки.
# slovar = {'login': 'Ivan', 'password':'123'}
# login = 'Ivan'
# password = '123'
# if login == slovar ['login'] and password == slovar [ 'password']:
#     print ('Доступ разрешён')
# else:
#     print (' Вы ввели неверное сочетание Login/ password')
# ==================================================
# 5. Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
# 3
# Hello Hi            Bye
# Bye Goodbye
# List Array
# Goodbye

# slovar = {}
# for i in range (3):
#     key, value = input().split()
#     slovar[key] = value
# print (slovar)
# a = input (' Введите слово:')
# for key,value in slovar.items():
#     if a == key:
#         print (value)
#     elif a == value:
#         print (key)
# =======================================
# 6. Дан текст: в первой строке задано число строк, далее идут сами строки.
#  Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# slovar = {}
# str = 'apple orange banana banana orange'.split(' ')
# print(str)
# for i in str:
#     slovar[i] = slovar.get(i, 0)+1
# print(slovar)
# maximum = max(slovar.values())
# minimum = 'z'
# for key, value in slovar.items():
#     if value == maximum:
#         if key<minimum:
#             minimum = key
# print(minimum)

