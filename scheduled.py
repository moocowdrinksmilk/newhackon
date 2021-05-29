# from database.database import Activity, User
import schedule
import time
import telegram
import config

bot = telegram.Bot(token=config.TOKEN) #Replace TOKEN with your token string


def send_scheduled_message(bot, user: User):
    
    activities = getAllActivitiesFromDatabase() # returns iterable of activities

    for activity in activities:
        if user_has_not_done_before(updater, user, activity): #check that user has not done before
            send_activity(bot=bot, user=user, activity=activity)
            return 
    
    # if here means user has completed all activities
    return 


def send_activity(bot, user: User, activity: Activity):
    bot.sendMessage(chat_id=user.chat_id, text=activity.toString()) #send activity content




def test_send():
    bot.sendMessage(chat_id=214291736, text="hello") #send activity content




# code for schedule

schedule.every(1).second.do(test_send)

while True:
    schedule.run_pending()
    time.sleep(1)
