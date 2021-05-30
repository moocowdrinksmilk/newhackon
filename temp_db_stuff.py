from database import userDAO
from datetime import datetime

# time = "06:45"
# userDAO.insert_user("214291736", "jonchuazh", datetime.datetime.strptime(time, '%H:%M'))
# print(userDAO.get_user("214291736"))



# userDAO.insert_user(chat_id="214291736", username="jonchuazh")
# userDAO.edit_set_time(chat_id="214291736", new_set_time = datetime.strptime('12:05', '%H:%M'))



# userDAO.delete("1")
# print("deleted")

print(userDAO.get_user("214291736"))
print(userDAO.get_user("214291736").set_time)
