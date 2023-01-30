def show_menu():
    print(' Выберите действие: \n 1 - показать всех сотрудников \n 2 - добавить сотрудника \n '
          '3 - удалить сотрудника \n 4 - выход ')
    select = int(input())
    return select


def show_result(msg):
    print(msg)


def add_man():
    print(' Введите Фамилию Имя Номер телефона сотрудника')
    man = input().split()
    return man


def del_men ():
    print(' Введите номер записи для удаления из файла ')
    number = int(input())
    return number


def show_members(people):
    print(' №\t Фамилия\t Имя \t Номер телефона')
    for i, p in enumerate(people):
        print(i, *p, sep="\t")
