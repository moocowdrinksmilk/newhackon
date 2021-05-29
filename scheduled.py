import schedule
import time


def send_scheduled():







# code for schedule

schedule.every(1).minute.do(send_scheduled)

while True:
    schedule.run_pending()
    time.sleep(1)
