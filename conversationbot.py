#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.1
"""

import logging
import config
from typing import Dict
import registration

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE = range(6)

start_keyboard = [
    ['Time', 'Duration'],
    ['Done'],
]

start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True)


def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""
    update.message.reply_text(
        "Hi! Welcome to TRYVE. What time would you like to TRYVE?",
        reply_markup=start_markup,
    )

    return CHOOSING_TIME

def time_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(f'What time?')
    text = update.message.text
    context.user_data['time'] = text

    return TIME_CHOICE

def duration_choice(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('How long? The recommended duration is 25 minutes')
    text = update.message.text
    context.user_data['duration'] = text

    return TIME_CHOICE
  
def received_time(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    user_data['time'] = text

    update.message.reply_text(
        f"Neat! We will suggest the activities at {user_data['time']}"    )
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('register', registration.register), 
                      CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Age|Favourite colour|Number of siblings)$'), registration.register_choice
                ),
                MessageHandler(Filters.regex('^Something else...$'), registration.reg_custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), registration.register_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), registration.received_information
                )
            ],
            CHOOSING_TIME: [
                MessageHandler(
                    Filters.regex('^Time$'), time_choice
                ),
                MessageHandler(
                    Filters.regex('^Duration$'), duration_choice
                )
            ],
            TIME_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), received_time
                )
            ],
            TIME_DONE: [
                MessageHandler(
                  Filters.regex('^Done'), start
                )
            ]
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), registration.done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()