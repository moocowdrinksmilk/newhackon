import schedule
import time
import telegram
import config
import datetime

from database.database import Activity, User
from database import activityDAO, userDAO

bot = telegram.Bot(token=config.TOKEN) #Replace TOKEN with your token string


def user_has_done_before(user: User, activity: Activity):
    for a in user.activities:
        if a.activity_id == activity.id:
            return True
    return False


def send_activity(bot, user: User, activity: Activity):
    bot.sendMessage(chat_id=user.chat_id, text=activity.content) #send activity content
    time.sleep(25 * 60) 
    bot.sendMessage(chat_id=user.chat_id, text=activity.prompt) #send activity content


def send_scheduled_message(bot, user: User):
    activities = activityDAO.get_all_activities() # returns list of all activities

    for activity in activities:
        if user_has_done_before(user, activity) and activity.category == 'solo' : #check that user has not done before
            print("ACTIVITY FOUND")
            send_activity(bot=bot, user=user, activity=activity)
            return 
    
    print("NO ACTIVITIES LA BODOH")
    # if here means user has completed all activities
    return 


def send_all_scheduled_messages(bot):
    users = userDAO.get_all_users
    now = datetime.datetime.now()

    # check that hour is the same
    for user in users:
        if user.set_time.hour == now.hour:
            if user.set_time.minute % 10 == now.hour.minute % 10:
                send_scheduled_message(bot=bot, user=user)
    


def test_send(bot): #send a message now!!!
    temp_user = User(chat_id=214291736, username="jon")
    send_scheduled_message(bot=bot, user=temp_user)
    bot.sendMessage(chat_id=214291736, text="reached here") #send activity content


test_send(bot=bot)


# run scheduler
schedule.every(10).minutes.do(send_activity)

while True:
    schedule.run_pending()
    time.sleep(1)
