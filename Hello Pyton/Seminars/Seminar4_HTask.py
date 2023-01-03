# Задача 1.
# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# from math import pi
# d = int(input("Введите точности числа Пи:"))
# print  (round(pi, d))
# ------------------------------------------------
#  Задача 2. Задайте натуральное число N.
#   Напишите программу, которая составит список простых множителей числа N.
# n = int(input(' Введите число:'))
# list = []
# d = 2
# while d * d <= n:
#         while n % d == 0:
#             list.append(d)
#             n //= d
#         d += 1
# if n > 1:
#         list.append(n)
# print (list)
# -------------------------------------------
# Задача 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [1,2,2,3,3,5,9,7,7,8,6,6]
# print(list)
# newList = []
# for i in list:
#     if list.count(i)<2:
#         newList.append(i)
# print (newList)
# ---------------------------------------------------
# Задача 4. Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k = int(input("Введите натуральную степень k = "))
# import random
# list = [random.randint(0, 101) for i in range(k+1)]
# kof = list
# def write_file(st):
#     with open('file.txt', 'w') as data:
#         data.write(st)

# def create_str(sp):
#     list = sp[::-1]
#     wr = ''
#     if len(list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
#                 wr += f'{list[i]}x^{len(list)-i-1}'
#                 if list[i+1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 wr += f'{list[i]}x'
#                 if list[i+1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 wr += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 wr += ' = 0'
#     return wr

# write_file(create_str(kof))
# ----------------------------------------------------

