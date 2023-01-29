
def get_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = input ('Введите номер телефона: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def writing_scv(info):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def writing_txt(info):
    file = 'Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

def from_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary