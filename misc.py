import logging
import config
from typing import Dict
import pprint
import datetime
from database import userDAO

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE, CHOOSING_START, PROMPT = range(8)

def record_prompt(update: Update, context: CallbackContext) -> int:
    print(update)
    user_id = update.message.chat.id
    prompt = update.message.text

    print(prompt)

    # userDAO.edit_set_time(user_id, parse_time)
    user = userDAO.get_user(user_id)
    update.message.reply_text(
        f"Neat! We will see you tomorrow at {user.set_time.time()}!")

    
    return ConversationHandler.END