import schedule
import time
import telegram
import config
import datetime

from database.database import Activity, User
from database import activityDAO, userDAO, userActivityDAO

# bot = telegram.Bot(token=config.TOKEN) 


def user_has_done_before(user: User, activity: Activity): # has user done activity before?
    for a in user.activities:
        if a.activity_id == activity.id:
            return True
    return False


def send_activity(bot, user: User, activity: Activity):
    print(user.chat_id)
    print(user)
    print(activity.title)
    bot.sendMessage(chat_id=user.chat_id, text="TRYVE ACTIVITIY OF THE DAY! \n\n"
                                                + activity.title + "\n" + activity.content)


def send_prompt(bot, user: User, activity: Activity):
    print(user.chat_id)
    print(user)
    print(activity.title)
    bot.sendMessage(chat_id=user.chat_id, text="DAILY TRYVE REFLECTION! \n\n"
                                                + activity.prompt + "\n\nSomething to say? Tell us your thoughts below!" )

    #add user-activity relationship
    userActivityDAO.insert_user_activity(user=user, activity=activity, score=1.0, reflection="nothing")


# functions to find activity the user has not done before
def find_new_activity(user: User): 
    activities = activityDAO.get_all_activities() 

    if len(user.activities) == len(activities):
        print("NO ACTIVITIES LA BODOH")
        return None

    for activity in activities:
        if not user_has_done_before(user, activity) and activity.category == 'solo':
            return activity
            
    
def send_scheduled_activity(bot, user:User):
    activity = find_new_activity(user=user)
    if activity is not None:
        print("ACTIVITY FOUND")
        send_activity(bot=bot, user=user, activity=activity)
        print("activity sent")
        return
    print("no activity found, so no message was sent")


def send_scheduled_prompt(bot, user:User):
    activity = find_new_activity(user=user)
    if activity is not None:
        print("PROMPT FOUND")
        send_prompt(bot=bot, user=user, activity=activity)
        print("prompt sent")
        return
    print("no activity found, so no message was sent")
    





# #functions to send all activities and prompts that are scheduled
# def send_all_scheduled_activities(bot=bot): 
#     users = userDAO.get_all_users()
#     now = datetime.datetime.now()
#     print(now)

#     # check the time
#     for user in users:
#         if user.set_time.hour == now.hour:
#             if int(user.set_time.minute / 10) == int(now.minute / 10):
                                
#                 activity = find_new_activity(user=user)
#                 if activity is not None:
#                     print("ACTIVITY FOUND")
#                     send_activity(bot=bot, user=user, activity=activity)
#                     print("activity sent")
#                     return
#                 print("no activity found, so no message was sent")




# def send_all_scheduled_prompts(bot=bot):
#     users = userDAO.get_all_users()
#     now = datetime.datetime.now()
#     print(now)

#     # check that time for prompt is the same
#     for user in users:
#         time_change = datetime.timedelta(seconds=30)
#         user_prompt_time = user.set_time + time_change

#         if user_prompt_time.hour == now.hour:
#             if int(user_prompt_time.minute / 10) == int(now.minute / 10):
#                 print("The time is same, sending prompt")

#                 activity = find_new_activity(user=user)
#                 if activity is not None:
#                     print("PROMPT FOUND")
#                     send_prompt(bot=bot, user=user, activity=activity)
#                     print("prompt sent")
#                     return
#                 print("no activity found, so no message was sent")
    
    






# # def test_send(bot): #send a message now!!!
# #     temp_user = User(chat_id=214291736, username="jon")
# #     send_scheduled_message(bot=bot, user=temp_user)
# #     bot.sendMessage(chat_id=214291736, text="reached here") #send activity content


# # test_send(bot=bot)


# # run scheduler
# schedule.every(1).minutes.do(send_all_scheduled_activities)
# schedule.every(1).minutes.do(send_all_scheduled_prompts)


# while True:
#     schedule.run_pending()
#     time.sleep(1)
