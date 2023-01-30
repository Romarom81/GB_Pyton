import csv


def get():
    with open('Staff.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
        return sp


def add_member(man):
    with open('Staff.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(man)


def del_member(number):
    with open('Staff.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';',)
        sp = list(reader)
    if number < len(sp):
        del sp[number]
        with open('Staff.csv', 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in sp:
                writer.writerow(row)
