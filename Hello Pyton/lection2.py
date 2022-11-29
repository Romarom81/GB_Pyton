# Как работать с файлами:
# Связать файловую систему с переменным файлом, 
# определив модификатор работы
#  a – открытие для добавления данных
#  r – открытие для чтения данных
#  w – открытие для записи данных
#  w+,r+


# colors =['red','green','blue','grey']
# data = open ('file.txt','a') # задается файл с именем и расширением, вторым аргументом задается модификатор
# data.writelines(colors) # хапишутся данные в файл без разделителей
# data.write ('line11\n')
# data.write ('line12\n')
# data.close()

# # второй вариант :
# with open ('file.txt','a') as data:
#     data.write ('1111\n')
#     data.write ('2222\n')

# Чтение данных с файла:
# path = 'file.txt'
# data = open (path,'r')
# for line in data:
#     print (line)
# data.close()


# ВЫЗОВ ФУНКЦИИ ИЗ ДРУГОГО МЕСТА(ФАЙЛА) 
# import helloPython
# print (helloPython.f(1)) # в скобках (файл из которог вызываем функцию.сама функция (аргумент))
# import helloPython as hi # можно присвоить сокращенное название файла (hi), и использовать его дальше
# print (hi.f(1))

# ДРУГИЕ ФУНКЦИИ:
# Функция Умножения строки или символа на число:
# def new_string (simbol, count =3):
#     return simbol*count
# print (new_string('!')) # печатает заданный символ count (по умолчанию заданный )раз. 
# print (new_string('?',6)) # печатает заданный символ, дополнительно заданный count раз. 
# print (new_string(4)) # печатает указанное значение count раз, в данном случае перемножает числа. 
# Функция Склеивания/собирания символов или строк
# def concatinatio (*params):
#     res: str = ''
#     for items in params:
#         res+=items
#     return res
 
# print (concatinatio('Привет, ', 'как ', 'дела ?')) # Привет, как дела
# print (concatinatio('a', '1', '#')) # a1#

# Функция Рекурсия
# def fib (n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range (5,10):
#     list.append (fib(e))
# print(list)

# Кортежи чисел
# a,b = 3,4  # обычное множественное присваиваение значений аргументам
# a = (3,5,9,52,41)  # кортеж чисел
# print (a) # выводит весь список 
# print (a[2]) # выводит конкретный элемент кортежа с индексом [2]
# print (a[-1])# выводит конкретный элемент кортежа с последним индексом [-1] 

#  СЛОВАРИ
# dictionary = {}  # создание пустого словаря
# dictionary = \
#     {
#         'up': "8",
#         'low': '2',
#         'left': '4',
#         'raight': '6'
#     }
# print(dictionary) # вывод всего словаря
# print (dictionary ['left']) # вывод одного ключа 
# for k in dictionary.keys ():  # вывод всех ключей словаря
#     print (k)

# for k in dictionary.values ():  # вывод всех значений словаря 
#     print(k)

# МНОЖЕСТВА (тип данных- set )
# colors = { 'red', 'green', 'blue'} # создание множества
# print (colors)
# colors.add ('grey')      # добавление элемента 
# print (colors)
# colors.remove ('red')   # удаление элемента 
# print (colors)
# colors.clear ()  # очистка множества 
# print (colors)

# a = {1,2,3,4,5,6}
# b = {6,7,8,9,10,11}
# с = a.copy ()  # копирование множества С
# u = a.union(b)  # объединение множеств


# Обратно к спискам 
list1 = [1,2,3,4,5]
list2 = list1
# for i in list1:
#     print(i)


# print()


# for i in list2:
#     print(i)

# list1[0]=123
# list2[-1]=555  # если меняешь один список, то меняется второй

# for i in list1:
#     print(i)


# print()


# for i in list2:
#     print(i)

# list1.pop() # удаление последнего элемента списка
# print(list1)

# list1.pop (1)  # удаление элемента с конкретным индексом
# print (list1)
# list1.insert(-1,11) # добавление элемента в конец списка? перед последним элементом/ Можно указать лбое место(индекс)
# print (list1)
# list1.append (12) # добавление последним элемента 
# print(list1)
