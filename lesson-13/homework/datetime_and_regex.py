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

#4
import pytz
from datetime import datetime

def timezone_converter(date_and_time, current_timezone, target_timezone):
    dt = datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')
    current_zone = pytz.timezone(current_timezone)
    current_dt = current_zone.localize(dt)
    target_zone = pytz.timezone(target_timezone)
    # c_dt = datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, tzinfo=current_zone)
    target = current_dt.astimezone(target_zone)

    return target
