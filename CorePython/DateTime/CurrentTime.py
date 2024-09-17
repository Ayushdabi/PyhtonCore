from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H,%M,%S")
print("current time is ",current_time)
print("current  date is ",now.date())

