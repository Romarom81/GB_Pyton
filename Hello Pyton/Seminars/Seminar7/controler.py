import view
import model
import logging

logging.basicConfig (level=logging.INFO) # для вывода лога в консоль

# вывод лога в файл log.txt 
# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(massage)s ',
#                     datefmt='%H:%M:%S',
#                     level=logging.INFO,
#                     encoding="utf-8")


def main_process():
    select = view.show_menu()
    if select == "1":
        logging.info(" Выбран режим калькулятор")
        i = view.get_x()
        res = model.culc(i)
        view.showresult(res)
        logging.info(" Результат выведен")
    elif select == "2":
        logging.info(" Выбран режим конвертор")
        m = view.get_m()
        res = model.convert(m)
        view.showresult_m(res)
        logging.info(" Результат выведен")
