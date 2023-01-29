def show_menu ():
    print ( ' Выберите раздел: \n 1- калькулятор \n 2 - конвертер ')
    select = input()
    return select

def get_x ():
    x = input ( ' Введите математический пример: ')
    return x

def get_m ():
    m = int(input('Введите массу:'))
    return m


def showresult (res):
    print (f" Результат вычислений = {res}")

def showresult_m (res):
    print (f' Maccа в граммах равна = {res} ')