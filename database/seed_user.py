import userDAO
from datetime import datetime

# time = "06:45"
# userDAO.insert_user("214291736", "jonchuazh", datetime.datetime.strptime(time, '%H:%M'))
# print(userDAO.get_user("214291736"))



# userDAO.insert_user(chat_id="214291736", username="jonchuazh")
userDAO.edit_set_time(chat_id="214291736", new_set_time = datetime.strptime('03:32', '%H:%M'))

print(userDAO.get_user("214291736"))

# userDAO.delete("1")
# print("deleted")