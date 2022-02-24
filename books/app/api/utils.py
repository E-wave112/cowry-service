from datetime import datetime
from datetime import timedelta


def date_in_string():
    """
    declare a defualt time in string when a new entity is created
    """
    return datetime.now().strftime("%d-%m-%Y, %H:%M:%S")


current_date = "12-6-20"


def add_days(date, days):
    date = date.strftime("%d-%m-%Y")
    date = datetime.strptime(date, "%d-%m-%Y")
    date += timedelta(days=days)
    return date.strftime("%d-%m-%y")
