# Reference: https://youtu.be/eirjjyP2qcQ?si=EG55I2zFGoa5dw2i
import datetime

"""
datetime.date
"""
# year, month, day
d = datetime.date(2025, 8, 26)
print(d)

tday = datetime.date.today()
print(tday)

print(tday.year, tday.month, tday.day)

print(tday.weekday())  # Monday 0, Sunday 6
print(tday.isoweekday())  # Monday 1, Sunday 7

# Timedelta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # 7 days from now
print(tday - tdelta)  # 7 days ago

bday = datetime.date(2025, 12, 3)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

"""
datetime.time
"""
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour, t.minute, t.second, t.microsecond)

"""
datetime.datetime
"""
# year, month, day, hour, minute, second, microsecond
dt = datetime.datetime(2025, 8, 26, 12, 30, 45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second, dt.microsecond)

# Now
now = datetime.datetime.now()
print(now)

# Time delta with datetime
tdelta = datetime.timedelta(hours=12)
print(now + tdelta)  # 12 hours from now

"""
strftime: Datetime to string (f for format)
strptime - String to Datetime (p for parse)
format reference: https://docs.python.org/3/library/datetime.html#format-codes
"""
print(now.isoformat())
print(now.strftime("%B %d, %Y"))  # Month Date, Year

dt_str = "August 26, 2025"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)

# Use pytz for timezone related operations
