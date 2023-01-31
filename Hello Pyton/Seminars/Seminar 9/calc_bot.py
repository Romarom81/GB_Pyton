from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint

bot_token = '6137461583:AAHZ3olOwSJlMawR1cCyOYPtLyWS43GHQrA'
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher 

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, я калькулятор! Выберите команду:"
    " /calc - решить пример, /conv - конвертировать /exit - выход ")

def exit (update, context):
    context.bot.send_message(update.effective_chat.id, "Пока, до новых встреч")

def calc (update, context):
    context.bot.send_message(update.effective_chat.id, "Введите выражение")
    return 1

def conv (update, context):
    context.bot.send_message(update.effective_chat.id, "Введите массу в кг")
    return 1

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

def Calculate (update, context):
    primer = update.message.text
    update.message.reply_text(
        f"Результат =  {eval(primer)}, Введите следующую команду:"
        "/calc - решить пример, /conv - конвертировать, или нажмите - stop ")
    
def Converter (update, context):
    massa = int(update.message.text)
    update.message.reply_text(
        f" Вес в граммах =  {massa*1000}, Введите следующую команду:"
        "/calc - решить пример, /conv - конвертировать, или нажмите - stop ")

calc_handler = ConversationHandler(
    entry_points=[CommandHandler('calc', calc)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, Calculate)]           
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('conv', conv)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, Converter)]           
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

start_handler = CommandHandler('start', start)
exit_handler = CommandHandler('exit', exit)
calc_handler = CommandHandler('calc', calc)
conv_handler = CommandHandler('conv', conv)
dispatcher.add_handler (conv_handler)
dispatcher.add_handler (calc_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler (calc_handler)
updater.start_polling()
updater.idle()