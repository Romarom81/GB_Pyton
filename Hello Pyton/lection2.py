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
