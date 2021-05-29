from sqlalchemy.orm import Session
from database import engine, Activity
from multipledispatch import dispatch

with Session(engine) as session:
    def get_activity_by_id(id):
        return session.query(Activity).get(id)

    def get_activity_by_title(title):
        return session.query(Activity).filter(title == title).first()

    def insert_activity(title, content, category, prompt):
        activity = Activity(title = title, content = content, category = category, prompt = prompt)
        session.add(activity)
        session.commit()

    def edit_content(title, new_content):
        session.query(Activity).filter(title == title).update({Activity.content: new_content})

    def edit_category(title, new_category):
        session.query(Activity).filter(title == title).update({Activity.category: new_category})

    def edit_prompt(title, new_prompt):
        session.query(Activity).filter(title == title).update({Activity.prompt: new_prompt})
        
