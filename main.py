import telegram
import config

bot = telegram.Bot(token=config.TOKEN) #Replace TOKEN with your token string
# print(bot.get_me())

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')


hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)


updater.start_polling()