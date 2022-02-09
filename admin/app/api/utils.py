from datetime import datetime


def date_in_string():
    '''
    declare a defualt time in string when a new entity is created
    '''
    return datetime.now().strftime("%d-%m-%Y, %H:%M:%S")