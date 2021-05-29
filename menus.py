
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
)
from database import userDAO

CHOOSING, TYPING_REPLY, TYPING_CHOICE, CHOOSING_TIME, TIME_DONE, TIME_CHOICE, CHOOSING_START = range(7)


start_keyboard = [
    ['Help!', 'Set TRYVE time'],
    ['Stop receiving suggestions'],
]

start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True)

def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.chat.id
    user = userDAO.get_user(user_id)
    if user is None:
        username = update.message.chat.username
        userDAO.insert_user(user_id, username, None)
        user = userDAO.get_user(user_id)
    update.message.reply_text(
        f"Hi {user.username}! Welcome to TRYVE. What would you like you to do?",
        reply_markup=start_markup,
    )
    return CHOOSING_START

def help(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Get Started\n"
        "/help - ask for help!\n"
        "/settime - set your daily TRYVE time\n"
        "/stop - stop receiving daily TRYVE activities\n"
    )

def stop(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "We will stop sending you suggestions again. Please press '/start' to use this bot again.\n"
        "⠁⠁⠁⠁⠁⠁⠐⢶⣶⣶⣶⣤⣤⡀⠁⠁⣠⣀⣀⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁\n"
        "⠁⠁⠁⠁⠁⠁⠁⠁⠙⢿⣯⣠⣶⣦⣤⣤⣌⣛⠻⢇⣠⣤⣤⠁⠁⠁⠁⠁⠁⠁\n"
        "⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⠻⣿⣿⣿⡟⢉⡤⢤⣤⣤⡍⠛⢡⢖⣥⣶⣦⣀⠁⠁\n"
        "⠁⠁⠁⠁⠁⠁⠁⠁⠁⠁⣠⣿⣿⣿⡏⣭⣶⣿⣿⠟⢿⣦⡡⣿⣿⡇⠁⡙⣷⡀\n"
        "⠁⠁⠁⠁⠁⠁⠁⣀⣴⣿⣿⣿⣿⣿⣿⡞⣿⣿⡟⢀⡀⣿⣿⢻⣿⣿⣀⣁⣿⠏\n"
        "⠁⠁⠁⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣟⢰⢻⣿⣇⣈⣴⣿⠟⢨⣛⠛⠛⠉⠁⠁\n"
        "⠁⣠⣶⣿⣿⡟⢋⠤⣤⠘⢿⣿⣧⡙⠻⠌⠒⠙⠛⢛⣫⣥⣿⣦⡈⠉⣡⣴⣾⠇\n"
        "⢰⣿⣿⣿⣿⠁⡇⠁⠙⠷⣤⡙⠻⢿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠁\n"
        "⠘⣿⣿⣿⣿⣆⠻⣄⠁⣀⡀⠉⠙⠒⠂⠉⠍⠉⠉⠉⠉⣩⣍⣁⣂⡈⠠⠂⠁⠁\n"
        "⠁⠘⢿⣿⣿⣿⣦⡉⠳⢬⣛⠷⢦⡄⠁⠁⠁⠁⠁⣀⣼⣿⣿⠿⠛⠋⠁⠁⠁⠁\n"
        "⠁⠁⠁⠉⠻⢿⣿⣿⣷⣦⣬⣍⣓⡒⠒⣒⣂⣠⡬⠽⠓⠂⠁⠁⠁⠁⠁⠁⠁⠁\n"
    )