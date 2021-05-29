from userDAO import *
from activityDAO import *
from userActivityDAO import *
from groupDAO import *
from groupActivityDAO import *
from datetime import datetime


#user
print("---------User------------")
#insert_user(1234,'rx9988')
# edit_username(1234,'rx8888')

# my_string = '11:00'
# first_time = datetime.strptime(my_string, "%H:%M")
# edit_set_time(1234,first_time)
print(get_user(1234))




#activity
print("---------Activity------------")
#insert_activity('cycling', 'learn how to cycle', 'single', 'have you been on a steroid cycle?')
# edit_prompt('cycling', 'do you like cycling')
print(get_activity_by_title('cycling'))
# print(get_activity_by_title('cycling').prompt)


#user activity
print("---------User Activity------------")
rx = get_user(1234)
activity = get_activity_by_title('cycling')
#insert_user_activity(rx,activity,5.0, 'i love cycling')

print(rx.activities[0].reflection)
print('---------------------')
edit_user_activity_reflection(rx,activity, 'i h8 cycling')
print(get_user_activity(rx,activity).reflection)

#group
print("---------Group------------")
#insert_group(69420)
actually_drink = get_group(69420)
print(actually_drink)

#group activity
print("---------Group Activity------------")
#insert_group_activity(actually_drink,activity, 3.8, 'it was interesting')
group_activity = get_group_activity(actually_drink, activity)
print(group_activity.reflection)
print(group_activity.score)
edit_group_activity_score(actually_drink, activity, 3.8)
print(actually_drink.activities[0].score)
