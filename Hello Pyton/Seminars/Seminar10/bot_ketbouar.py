import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '6137461583:AAHZ3olOwSJlMawR1cCyOYPtLyWS43GHQrA'


def start(update, context):
    update.message.reply_text(
        "привет, как дела? Чем Вам помочь?",
        reply_markup=markup
    )

def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )

def help(update, context):
    update.message.reply_text(
        "Вам нужна помощь? ")


def address(update, context):
    update.message.reply_text(
        " адрес: Москва, ул. Вавилова , дом 32 а")


def phone(update, context):
    update.message.reply_text("Телефон: 8 (800) 555-15-40")


def site(update, context):
    update.message.reply_text(
        "сайт: https://gb.ru")


def work_time(update, context):
    update.message.reply_text(
        "Работаем круглосуточно.")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()