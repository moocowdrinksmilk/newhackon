from database.sessionStart import session
from database.database import engine, User

def get_user(chat_id):
    return session.query(User).get(chat_id)

def insert_user(chat_id, username, set_time = None):
    user = User(chat_id = chat_id, username = username, set_time= set_time)
    session.add(user)
    session.commit()

def edit_username(chat_id, new_username):
    session.query(User).filter(chat_id == chat_id).update({User.username: new_username})
    session.commit()

def edit_set_time(chat_id, new_set_time):
    session.query(User).filter(chat_id == chat_id).update({User.set_time: new_set_time})
    session.commit()
        
def get_all_users():
    return session.query(User).all()


def delete(chat_id):
    user = get_user(chat_id)
    session.delete(user)
    session.commit()