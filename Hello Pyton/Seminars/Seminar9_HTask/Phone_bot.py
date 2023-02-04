from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler
from Token import TOKEN
# from modelCSV import *
from modelSQL import *
import sqlite3

bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher 

conn = sqlite3.connect('List_personal.db', check_same_thread=False) 
cursor = conn.cursor()

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет,я справочник, Введите команду:\n"
    " /show - показать все записи\n"
    " /find - поиск сотрудника\n "
    " /add - добавить запись\n "
    " /delete - удалить запись из таблицы\n  "
    " /exit - выход\n ")

def exit (update, context):
    context.bot.send_message(update.effective_chat.id, "Пока, возвращайтесь!")

def stop (update, context):
    return ConversationHandler.END

def show (update, context):
    data = view_all (cursor)
    context.bot.send_message(update.effective_chat.id, f"{data}")

def request (update, context):
    context.bot.send_message(update.effective_chat.id, " Введите фамилию или имя сотрудника: \n")
    return 1

def find (update, context):
    item = update.massage.text
    data = find_men(item, cursor)
    context.bot.send_message(update.effective_chat.id, f'{data}')

def add (update, context):
    context.bot.send_message(update.effective_chat.id,'Введите Фамилию, Имя, Номер телефона' )
    data = update.massage.text
    res = add_man (data, conn, cursor)
    context.bot.send_message(update.effective_chat.id,f'Запись успешно добавлена, новый список: \n {show}' )


def delete (update, context):
    context.bot.send_message(update.effective_chat.id, 'ВВедите ID сотрудника:')
    id_man = update.massage.text
    msg = dell (id_man, conn, cursor)
    context.bot.send_message(update.effective_chat.id, msg)

start_handler = CommandHandler('start', start)
exit_handler = CommandHandler('exit', exit)
show_handler = CommandHandler('show', show)
find_handler = CommandHandler('find', find)
add_handler = CommandHandler('add', add)
delete_handler = CommandHandler('delete', delete)

dispatcher.add_handler (delete_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler (find_handler)
dispatcher.add_handler (add_handler)
updater.start_polling()
updater.idle()