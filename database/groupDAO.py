from sessionStart import session
from database import engine, User

def get_group(chat_id):
    return session.query(Group).get(chat_id)

def insert_group(chat_id, set_time = None):
    group = Group(chat_id = chat_id, set_time= set_time)
    session.add(group)
    session.commit()


def edit_set_time(chat_id, new_set_time):
    session.query(Group).filter(chat_id == chat_id).update({Group.set_time: new_set_time})
    session.commit()
        
