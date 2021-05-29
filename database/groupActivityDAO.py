from database.sessionStart import session
from database.database import engine, GroupActivity
from database.activityDAO import *
from database.groupDAO import *

def get_group_activity(group,activity):
    return session.query(GroupActivity).filter(GroupActivity.group == group, GroupActivity.activity == activity).first()

def insert_group_activity(group,activity,score, reflection):
    group_activity = GroupActivity(group = group, activity = activity, score = score, reflection = reflection)
    session.add(group_activity)
    session.commit()

def edit_group_activity_score(group,activity,new_score):
    session.query(GroupActivity).filter(GroupActivity.group == group, GroupActivity.activity == activity).update({GroupActivity.score: new_score})
    session.commit()
    
def edit_group_activity_reflection(group,activity,new_reflection):
    session.query(GroupActivity).filter(GroupActivity.group == group, GroupActivity.activity == activity).update({GroupActivity.reflection: new_reflection})
    session.commit()