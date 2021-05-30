from sqlalchemy.orm import Session
from database.database import engine

session = Session(engine)