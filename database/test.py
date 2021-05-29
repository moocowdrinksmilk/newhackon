from sqlalchemy.orm import Session
from database.database import engine, User, Group, Activity, UserActivity, GroupActivity


with Session(engine) as session:
    user = User(username="GPeabody")
    session.add(user)
    session.commit()
    gary = session.query(User).filter_by(username="GPeabody").first()
    print(gary)


    activity = Activity(title="juggling")
    session.add(activity)
    session.commit()
    juggling = session.query(Activity).filter_by(title="juggling").first()
    print(juggling)



    userActivity = UserActivity(user = gary, score=1, reflection="I quite liked it", activity = juggling)
    session.add(userActivity)
    session.commit()
    garyjugs = session.query(UserActivity).first()
    print("useractivity")
    print(garyjugs.user_id)
    print(garyjugs.activity_id)

    a_li = []

    for a in gary.activities:
        a_li.append(a.activity_id)

    print(a_li)
