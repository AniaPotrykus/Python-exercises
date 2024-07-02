#Write a simple function that takes as a parameter a date object and returns a boolean value representing whether the date is today or not.

#Make sure that your function does not return a false positive by only checking the day.

from datetime import datetime

def is_today(date):
    today = datetime.today()
    return today.year == date.year and today.month == date.month and today.day == date.day
    

