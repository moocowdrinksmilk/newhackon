import database

database.User.__table__.drop(database.engine)
database.Group.__table__.drop(database.engine)
database.UserActivity.__table__.drop(database.engine)
database.GroupActivity.__table__.drop(database.engine)
database.Activity.__table__.drop(database.engine)

