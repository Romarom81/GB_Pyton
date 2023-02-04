import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, Filters, MessageHandler
import random

quallity_candies = 0

reply_keyboard = [['/rules', '/game'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )

# logger = logging.getLogger(__name__)

TOKEN = '6137461583:AAHZ3olOwSJlMawR1cCyOYPtLyWS43GHQrA'

def start(update, context):
    update.message.reply_text(
        f"Привет, сыграем?\n",
        " /game - начать игру \n"
        " /rules - правила игры \n"
        " /exit - выйти из игры \n",
        reply_markup=markup
    )

def game (update, context):
    update.message.reply_text(
        " ВВедите количество конфет для начала игры",
        reply_markup=ReplyKeyboardRemove()
    )
    return 1

def rules(update, context):
    update.message.reply_text(
        " 1. Игроки ходят по очереди\n"
        " 2. Игрок может брать не более 28 конфет за ход]\n"
        " 3. Выиграл тот, кто взял последние конфеты")


def exit(update, context):
    update.message.reply_text(
        " Пока, возвращайтесь!",
        reply_markup=ReplyKeyboardRemove()
    )


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def init_game (update, context):
    global quallity_candies
    quallity_candies = update.message.text
    update.message.reply_text(f"На кону {quallity_candies} конфет \n "
    " Ваш ход, сколько конфет возьмёте?")
    return 2

def next_move (update, context):
    global quallity_candies
    qulity_candies_pleyer = update.message.text
    quallity_candies = quallity_candies - qulity_candies_pleyer
    if quallity_candies >= 29:
        update.message.reply_text (f'На кону остаток {quallity_candies } конфет \n'
        ' Мой ход: ')
        qulity_candies_bot = random.randint (1,29)
        update.message.reply_text (f'Я беру {qulity_candies_bot} конфет, Ваш ход')
        quallity_candies = quallity_candies - qulity_candies_bot
        if quallity_candies >= 29:
            update.message.reply_text (f'На кону остаток {quallity_candies } конфет \n')
            update.message.reply_text(f"Ваш ход, сколько конфет возьмёте?")
            return 2
        else:
            update.message.reply_text (' Поздравляю, Твоя победа!!')
    else:
        update.message.reply_text (' Моя победа')
    return ConversationHandler.END


game_handler = ConversationHandler (
entry_points= [ CommandHandler("game", game)] , 
    states = {
        1: [MessageHandler(Filters.text & ~Filters.command, init_game)],
        2: [MessageHandler(Filters.text & ~Filters.command, next_move)],
        }, 

    fallbacks=[CommandHandler('stop', stop)]
)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
