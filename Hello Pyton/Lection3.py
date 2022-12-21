# def f(x):
#     return x**2
# g = f
# print (f(4))
# print (g(4))

# print (type(f)) # тип функции
# print (type(g)) # тип переменной в которую переданна функция

# def calc1 (x):
#     return x+10

# def calc2 (x):
#     return x**2

# def math (op,x):    # фйнкция, которая вызывает другую функцию calc1 или calc2, с передачей аргумента (x)
#     print (op(x))

# math (calc1,10)
# math (calc2,10)

# =====================================

# def sum (x , y):
#     return x+y

# sum = lambda x,y: x+y  # выражение по функционалу тоже самое что выше записано

# def multi (x,y):
#     return x*y

# def calc (op, a,b):
#     # return op(a,b)
#     print (op(a,b))

# # calc (sum,4,5)
# calc (lambda x,y : x+y +2 , 4,5) # можно уместить все в одну строку

# =======================================
# LIst Comprehantion
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp (if conditional) for item in iterable (if conditional)] # на старте лучше НЕ использовать

# list = []
# for i in range (1,21):
#     if i%2 == 0:
#         list.append (i)
# print (list)

# list = [i for i in range (1,21) if i%2 == 0 ]  # тоже самое что сверху , только в одну строку

# list = [(i,i) for i in range (1,21) if i%2 == 0 ] # получаем список картежей

# def f (x):
#     return x**3
# list = [f(i) for i in range (1,21) if i%2 == 0 ]
# list = [(i,f(i)) for i in range (1,21) if i%2 == 0 ]

# print (list)

# def select(f, col):
#  return [f(x) for x in col]


# def where(f, col):
#  return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list (select(lambda e: (e, e**2), data))
