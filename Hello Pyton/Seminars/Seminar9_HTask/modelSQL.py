import sqlite3

conn = sqlite3.connect('List_personal.db')
cursor = conn.cursor()

def view_all(cursor):
    cursor.execute('select * from List_personal')
    results = cursor.fetchall()
    return results


def find_men(item, cursor):
    cursor.execute(f'select * from List_personal where surname like "%{item}%"'
    f'or name like "%{item}%"')
    results = cursor.fetchall()
    if results:
        return results
    return " Нет резальтатов "

def add_man (data, conn, cursor):
    surname,name,phone = data
    cursor.execute (f'insert into List_personal (surname,name,phone)'
    f'values ("{surname}","{name}", {phone}," ")')
    conn.commit()

def dell (id, conn, cursor):
    try:
        cursor.execute (f'delete from List_personal where id={id}')
        conn.commit()
        return " Контакт удален"
    except:
        return " Контакт не найден, введите другой id"


conn.close()