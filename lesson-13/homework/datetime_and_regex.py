#1 Age calculator
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def age(birth_date):
    dob = dt.strptime(birth_date, '%Y-%m-%d')
    today = dt.today()
    diff = relativedelta(today, dob)
    return f"You a are {diff.years} year(s), {diff.months} month(s) and {diff.days} day(s) old"
