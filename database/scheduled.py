import schedule
import time
import telegram
import config
import datetime

from database import Activity, User
import activityDAO, userDAO

bot = telegram.Bot(token=config.TOKEN) #Replace TOKEN with your token string


def user_has_done_before(user: User, activity: Activity):
    for a in user.activities:
        if a.activity_id == activity.id:
            return True
    return False


def send_activity(bot, user: User, activity: Activity):
    print(user.chat_id)
    print(user)
    print(activity.title)
    bot.sendMessage(chat_id=user.chat_id, text=activity.content) #send activity content
    time.sleep(5) 
    bot.sendMessage(chat_id=user.chat_id, text=activity.prompt) #send activity content


def send_scheduled_message(bot, user: User):
    activities = activityDAO.get_all_activities() # returns list of all activities

    for activity in activities:
        if not user_has_done_before(user, activity) and activity.category == 'solo' : #check that user has not done before
            print("ACTIVITY FOUND")
            send_activity(bot=bot, user=user, activity=activity)
            return 
    
    print("NO ACTIVITIES LA BODOH")
    # if here means user has completed all activities
    return 


def send_all_scheduled_messages(bot=bot):
    print("Trying to send message")
    users = userDAO.get_all_users()
    now = datetime.datetime.now()
    print()
    print(now)
    print()

    # check that hour is the same
    for user in users:
        # print("checking user " + user.username)
        # print("This is the user hour " +  str(user.set_time.hour))
        # print("This is now hour " + str(now.hour))
        if user.set_time.hour == now.hour:
            # print("The hour is correct%n%n")
            # print("This is user minute " + str(int(user.set_time.minute / 10)))
            # print("This is the minute " + str(int(now.minute / 10)))
            if int(user.set_time.minute / 10) == int(now.minute / 10):
                print("The time is same, sending message")

                send_scheduled_message(bot=bot, user=user)
                print("message sent")
    


# def test_send(bot): #send a message now!!!
#     temp_user = User(chat_id=214291736, username="jon")
#     send_scheduled_message(bot=bot, user=temp_user)
#     bot.sendMessage(chat_id=214291736, text="reached here") #send activity content


# test_send(bot=bot)


# run scheduler
schedule.every(5).seconds.do(send_all_scheduled_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
