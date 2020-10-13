import calendar
import datetime

now = datetime.datetime.now()
y = int(now.year)
m = int(now.month)

c = calendar.HTMLCalendar()
data = c.formatmonth(y,m)
print(data)