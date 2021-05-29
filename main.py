import telegram

bot = telegram.Bot(token='1818728332:AAHth8z7BIa3sVcjIvmgeaVn9kFBoMIzBQs') #Replace TOKEN with your token string
# print(bot.get_me())

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1818728332:AAHth8z7BIa3sVcjIvmgeaVn9kFBoMIzBQs', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')


hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)


updater.start_polling()