# № 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# list = [1, 3, 4, 7, 9, 12, 4, 3, 16]
# sum = 0
# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
# print(sum)
#  № 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list2 = [2, 3, 4, 5, 6]
# newlist = []
# for i in range(len(list2)+1//2):
#     newlist.append(list2[i] * list2[-i-1])
# print(newlist)

# № 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# sp = [1.1, 1.2, 3.1, 5, 10.01]
# sp1 =[]
# for i in range(5):
#     sp1.append (sp[i]-int(sp[i]))
# print(max(sp1)-min(sp1))

# № 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное
#  например 45 -> 101101

# a = int(input(" Введите число "))
# list = []
# while a > 0:
#     list.append(a % 2)
#     a //= 2
# print(*list)

# № 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример: k = 8

k = 8
fib = [0, 1]
for i in range (2, k+1):
    fib.append (fib[-1] + fib[-2])
for i in range (k):
    fib.insert ( 0, fib[1] - fib[0])
print(fib)