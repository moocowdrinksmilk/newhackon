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
import times
import menu
from database import userDAO
import datetime
import scheduled
from apscheduler.schedulers.background import BackgroundScheduler

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

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE, CHOOSING_START, PROMPT, RECEIVED_PROMPT = range(9)


sched = BackgroundScheduler()
sched.start()

def received_time(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    print(update)
    user_id = update.message.chat.id
    time = update.message.text

    parse_time =  datetime.datetime.strptime(time, '%H:%M')
    job = sched.add_job(scheduled.send_scheduled_activity, 'cron', [update, context],hour=parse_time.hour, minute=parse_time.minute)
    job = sched.add_job(scheduled.send_scheduled_prompt, 'cron', [update, context],hour=parse_time.hour, minute=parse_time.minute, second=15)
    print(parse_time)

    userDAO.edit_set_time(user_id, parse_time)

    update.message.reply_text(
        f"Neat! We will suggest the activities at {parse_time.time()}")

    return RECEIVED_PROMPT

def received_prompt(update: Update, context: CallbackContext) -> int:
    user_id = update.message.chat.id
    prompt = update.message.text
    user = userDAO.get_user(user_id)


    update.message.reply_text(
            f"Neat! We see you at {user.set_time.time()} tomorrow")
    
    return ConversationHandler.END

def main():
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('register', registration.register), 
        CommandHandler('start', menu.start),
        CommandHandler('settime', times.settime),
        CommandHandler('help', menu.help),
        CommandHandler('stop', menu.stop)],
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
                    Filters.regex('^Time$'), times.time_choice
                ),
                MessageHandler(
                    Filters.regex('^Duration$'), times.duration_choice
                )
            ],
            TIME_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), received_time
                )
            ],
            TIME_DONE: [
                MessageHandler(
                  Filters.regex('^Done$'), times.received_time
                )
            ],
            CHOOSING_START: [
                MessageHandler(
                    Filters.regex('^Help!$'), menu.help
                ), 
                MessageHandler(
                    Filters.regex('^Set TRYVE time$'), times.settime
                ),
                MessageHandler(
                    Filters.regex('^Stop receiving suggestions$'), menu.stop
                )
            ], 
            RECEIVED_PROMPT: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), received_prompt
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
