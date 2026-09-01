import datetime

date = datetime.date(2025, 10, 4)
print(date)
# Returns how/what you wanted the date to be

today = datetime.date.today()
print(today)
# Returns actually what you wanted the date to be

time = datetime.time(5, 00, 30)
print(time)
# Returns how/what you wanted the time to be

now = datetime.datetime.now()
print(now)
# Returns actually what you wanted the time to be

# Formats the datetime string in the manner how it's returned!!!
now = now.strftime("%H:%M:%S %d/%m/%Y")
print(now)

target_datetime = datetime.datetime(2020, 2, 3, 12, 45, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed!")
else:
    print("Target date has not yet passed!")