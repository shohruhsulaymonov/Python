#1 Age calculator
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def age(birth_date):
    dob = dt.strptime(birth_date, '%Y-%m-%d')
    today = dt.today()
    diff = relativedelta(today, dob)
    return f"You a are {diff.years} year(s), {diff.months} month(s) and {diff.days} day(s) old"
#2 Next Birtday calculator
from datetime import datetime as dt, date
def next_bd(dob):
    dob = dt.strptime(dob, '%Y-%m-%d')
    today = dt.today().date()
    next_bd = None
    if (dob.month < today.month) or (dob.month == today.month and dob.day < today.day):
        next_bd = date(today.year + 1, dob.month, dob.day)
    else:
        next_bd = date(today.year, dob.month, dob.day)
    diff = next_bd - today
    diff = diff.days
    if diff == 0:
        return "Today is your Birthday!"
    else:
        return f"Your next Birthday is in {diff} day(s)"
#3
current = input('Please, enter the current date and time(YYYY-mm-dd HH:MM): ')
current = datetime.strptime(current, '%Y-%m-%d %H:%M')
duration = input('How long does the meeting last (HH-MM)?: ')
duration = datetime.strptime(duration, '%H:%M')
hours = duration.hour
minutes = duration.minute
time_to_add = timedelta(hours=hours, minutes=minutes)
end_time = current + time_to_add
print(end_time)
#4
import pytz
from datetime import datetime

def timezone_converter(date_and_time, current_timezone, target_timezone):
    dt = datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')
    current_zone = pytz.timezone(current_timezone)
    current_dt = current_zone.localize(dt)
    target_zone = pytz.timezone(target_timezone)
    target = current_dt.astimezone(target_zone)

    return target
#5
def countdown(fdate):
    future_date = datetime.strptime(fdate, '%Y-%m-%d %H:%M:%S')
    while True:
        now = datetime.now().replace(microsecond=0)
        diff = future_date - now

        print(diff)
        t.sleep(1)
        if not diff:
            print("Time is up!")
            break
