import userDAO
import datetime

time = "14:00"
# userDAO.insert_user("355189004", "bingyuyap", datetime.datetime.strptime(time, '%H:%M'))
print(userDAO.get_user("355189004"))