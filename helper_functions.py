import datetime
import math
import matplotlib.pyplot as plt

def get_epoch_time(time_string):
    year = 2000 + int(time_string[0:2]) if int(time_string[0:2]) < 30 else 1900 + int(time_string[0:2])
    doy = int(time_string[2:5])
    day_frac = float(time_string[5:])
    month = (datetime.datetime(year,1,1) + datetime.timedelta(days=doy-1)).month
    day = (datetime.datetime(year,1,1) + datetime.timedelta(days=doy-1)).day
    hour = math.floor(day_frac * 24.)
    minute = math.floor((day_frac * 24 * 60) % 60)
    second = math.floor((day_frac * 24 * 3600) % 60)

    epoch_time = datetime.datetime(year, month, day, hour, minute, second)
    return epoch_time

def make_difference_plot():
    pass