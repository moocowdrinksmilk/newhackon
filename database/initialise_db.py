import database

database.User.__table__.create(database.engine)
database.Group.__table__.create(database.engine)
database.UserActivity.__table__.create(database.engine)
database.GroupActivity.__table__.create(database.engine)
database.Activity.__table__.create(database.engine)

