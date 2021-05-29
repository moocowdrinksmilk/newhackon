import logging
import config
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE = range(6)

settime_keyboard = [
    ['Time', 'Duration'],
    ['Done'],
]

settime_markup = ReplyKeyboardMarkup(settime_keyboard, one_time_keyboard=True)

def settime(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""
    update.message.reply_text(
        "Hi! Welcome to TRYVE. What time would you like to TRYVE?",
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
  
def received_time(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    user_data['time'] = text

    update.message.reply_text(
        f"Neat! We will suggest the activities at {user_data['time']}"    )
    return ConversationHandler.END