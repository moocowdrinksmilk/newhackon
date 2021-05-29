import telegram
from telegram.utils.helpers import effective_message_type
import config

bot = telegram.Bot(token=config.TOKEN) #Replace TOKEN with your token string
# print(bot.get_me())

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World', reply_markup=main_menu_keyboard())
    print(update.effective_chat.id)

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Menu 1', callback_data='m1')],
              [InlineKeyboardButton('Menu 2', callback_data='m2')],
              [InlineKeyboardButton('Menu 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text="First menu",
                        reply_markup=first_menu_keyboard())


hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))


updater.start_polling()