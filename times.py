import logging

from sqlalchemy.sql.functions import user
import config
from typing import Dict
import pprint
import datetime
from database import userDAO
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

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE, CHOOSING_START = range(7)

settime_keyboard = [
    ['Time', 'Duration'],
    ['Done'],
]

settime_markup = ReplyKeyboardMarkup(settime_keyboard, one_time_keyboard=True)

sched = BackgroundScheduler()
    
sched.start()

def settime(update: Update, context: CallbackContext) -> int:

    """Start the conversation and ask user for input."""
    user_id = update.message.chat.id
    user = userDAO.get_user(user_id)

    if user is None:
        print('new user')
        username = update.message.chat.username
        userDAO.insert_user(user_id, username, None)
    update.message.reply_text(
        f"Hi {user.username}! Welcome to TRYVE. What time would you like to TRYVE?",
        reply_markup=settime_markup,
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
  
