from view import *
from model import *


def main():
    while True:

        select = show_menu()

        if select == 1:
            people = get()
            show_members(people)
        elif select == 2:
            man = add_man()
            add_member(man)
            show_result(' Запись добавлена')
        elif select == 3:
            member = del_men()
            del_member(member)
            show_result(' Запись удалена')
        elif select == 4:
            show_result (' До встречи')
            break

