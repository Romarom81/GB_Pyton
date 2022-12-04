# print ('hello python')
# типы данных и пременные
# int, float, boolean, str, list, None

# a = 123
# b = 1.236
# print (a) # вывод данных
# print (b) # вывод данных
# s = 'hello world'
# print (s) # вывод строки
# print (a, b, s) # вывод нескольких данных в одну строку
# print (a,'-', b,'-',s) # еще один вариант вывода данных
# print ('{}-{}-{}'.format (a,b,s)) # еще один вариант вывода данных
# print (f'{a}-{b}-{s}') # и еще один вариант вывода данных
# f = False
# print (f)

# объявление списка
# list = [1,2,3,4,5]
# print (list)

# команда print выводит данные
# команда input забирает данные (ввод данных)
# print ('введите значение а:')
# a = input ()
# print (' введите значение b:')
# b = input ()
# print (a,b)
# print ('{} {}'.format (a,b))
# print (f'{a} {b}')
# print (a, '+' ,b, '=' ,a+b)
# если мы захотим вывести результат примера, то ничего не получится
# т.к по умолчанию тип данных строка т.к он не объявлен

# для того, чтобы поменять тип данных, его необходимо прописать перед вводом, например:
# print ('введите значение а:')
# a = int(input())
# print ('введите значение b:')
# b = int(input ())
# print (a, '+' ,b, '=' ,a+b)

# или так,

# print ('введите значение а:')
# a = float(input())
# print (' введите значение b:')
# b = float(input ())
# print (a,'+',b,'=',a+b)

# можно объявить список с разными типами данных, например:
# list = ['hello',1.2,1,2,3,4,4.5,True]
# print (list)


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# + - сложение
# - - вычетание
# * - умножение
# / - деление, по умолчанию для вещественных чисел, т.е 2/8=0,25
# % - получение остатка от деления
# // - целочисленное деление без остатка
# ** - возведение в степень
# **, ⊕, ⊖, *, /, //, +,-    --  приоритетность операций
# приоритетность могут менять обычные ()
# round - функция округления
# пример,
# a = 2
# b = 16
# с = a/b
# print (с)
# a = 2
# b = 16
# с = round (a/b,2)
# print (с)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ

#  >, >=, <, <=, ==, !=not, and, or – не путать с &, |, ^

# Кое-что ещё: is, is not, in, not in


# УПРАЫВЛЯЮЩИЕ КОНСТРУКЦИИ:if, if-else
#        опрератор If / else :
# a = int(input('введите число a = '))
# b = int(input('введите число b = '))
# if a>b:
#     print ("наибольшее число",a)
# else:
#     print ("наибольшее число", b)
#       оператор if / elif / else
# username = input('Ведите имя пользователя:  ')
# if username == 'Маша':
#     print(" Ура , это же Маша!!")
# elif username == 'Марина':
#     print(" я так ждала Вас, Марина")
# elif username == 'Ильнар':
#     print(" Ильнар, Вы топчик!!")
# else:
#     print (' Привет,', username)

# УПРАЫВЛЯЮЩИЕ КОНСТРУКЦИИ, WHILE 

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original%10)
#     original//=10
# else:
#     print('пожалуй ,хватит,')
#     print ('достаточно!')
# print(inverted)

# УПРАЫВЛЯЮЩИЕ КОНСТРУКЦИИ, FOR
# list = [1,2,3,4,5,6]
# for i in list:
#     print(i**2)

# или
# for i in range(5): # range - создание ранжированного списка до указанного значения
#     print (i**3)

# for i in range(5,25,2): # список от 5 до 25 с шагом 2 (три аргумента)
#     print(i)



# НЕМНОГО О СТРОКАХ:
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) #количество символов в строке
# print('ещё' in text) # проверка налочия определенных символов в строке 
# print(text.isdigit()) # проверка являются ли символы цифрами
# print(text.islower()) # проверка являются ли символы нижним регистром (прописными)
# print(text.replace('ещё','ЕЩЁ')) # замена символа или группы символов  в строке на другой
# for c in text:
#     print(c)
# print(text[0]) # с
# print(text[1]) # ъ
# print(text[len(text)-1]) # k
# print(text[6:-18]) # ещё этих мягких

# СПИСКИ , ВВЕДЕНИЕ:

## list = list

# numbers =[1,2,3,4,5]  # стандартное создание списка
# print(numbers)
# print (type(numbers))
# ran = range (5,11) # список  через рендж, но у него соотвествующий формат, который нужно привести в лист
# print (type(ran))
# numbers = list(ran)
# print (type(numbers))
# numbers[0]=10 # замена элемента под индексом [0]
# print(numbers)
# print (len(numbers)) # вывод длины списка
# for i in numbers: # работа со спписком сам список не меняет
#     i*=2
#     print (i)
# print (numbers) # после работы список прежний

# доп функции работы со списками:
# colors = ['red', 'green', 'blue']
# for i in colors:      # перебираем элементы и печатаем, в данном случае элемент = слово(цвет)
#     print(i) # red green blue
# colors.append('gray') # добавить в конец элемент 
# print (colors)
# colors.remove('red') # удалить элемент
# # del colors[0] # или так удалить элесмент
# print (colors)

# СОЗДАНИЕ ФУНКЦИИ 
# def Function_name (arguments):
#     body line 1
#     .....
#     body line N
#     return - опционально 

# пример:
# def f (x):
#     if x==1:
#         return 'Целое'
#     elif x==2.3:
#         return 23
#     else:
#         return
# arg =2
# print (f(arg))
# print (type(f(arg)))