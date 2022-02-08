import datetime

from datetime import datetime


def date_in_string():
    '''
    declare a defualt time in string when a new entity is created
    '''
    return datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

current_date = "12-6-20"
def add_days(date, days):
    date = datetime.datetime.strptime(date, "%d-%m-%y")
    date += datetime.timedelta(days=days)
    return date.strftime("%d-%m-%y")