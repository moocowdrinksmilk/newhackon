from database.sessionStart import session
from database.database import engine, UserActivity
from database.activityDAO import *
from database.userDAO import *

def get_user_activity(user,activity):
    return session.query(UserActivity).filter(UserActivity.user == user, UserActivity.activity == activity).first()

def insert_user_activity(user,activity,score, reflection):
    user_activity = UserActivity(user = user, activity = activity, score = score, reflection = reflection)
    session.add(user_activity)
    session.commit()

def edit_user_activity_score(user,activity,new_score):
    session.query(UserActivity).filter(UserActivity.user == user, UserActivity.activity == activity).update({UserActivity.score: new_score})
    session.commit()
    
def edit_user_activity_reflection(user,activity,new_reflection):
    session.query(UserActivity).filter(UserActivity.user == user, UserActivity.activity == activity).update({UserActivity.reflection: new_reflection})
    session.commit()