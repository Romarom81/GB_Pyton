# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# list = [int(i) for i in input().split() ]
# for e in list:
#     if list.count(e)==1:
#         print(e)

# 2. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
# list = [int(i) for i in input().split() ]
# for i in range (len(list)-1):
#     if list[i]<list[i+1]:
#         print (list[i+1], end = ' ') # end = ' ' выывод в одну строчку через пробел
       
# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime
# import time


# def my_random (x):
#     t = str(time. time())[-x:]
#     print (t)


# my_random(5)
