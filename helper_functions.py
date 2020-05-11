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

def make_difference_plot(stk_data, python_data):
    times = []
    
    stk_pos_x = []
    stk_pos_y = []
    stk_pos_z = []

    python_pos_x = []
    python_pos_y = []
    python_pos_z = []

    for ephem in stk_data['ephemeris_list']:
        times.append(ephem['time'])
        stk_pos_x.append(ephem['position'][0] / 1000.)
        stk_pos_y.append(ephem['position'][1] / 1000.)
        stk_pos_z.append(ephem['position'][2] / 1000.)

    for ephem in python_data['ephemeris_list']:
        python_pos_x.append(ephem['position_pef'][0])
        python_pos_y.append(ephem['position_pef'][1])
        python_pos_z.append(ephem['position_pef'][2])

    assert len(stk_pos_x) == len(python_pos_x), str.format('STK and Python X array lengths ({} {}) do not match'.format(len(stk_pos_x), len(python_pos_x))) 
    assert len(stk_pos_y) == len(python_pos_y), 'STK and Python Y array lengths do not match'
    assert len(stk_pos_z) == len(python_pos_z), 'STK and Python Z array lengths do not match'
    assert len(times) == len(stk_pos_x), 'Time and position array lengths do not match'

    diff_x = [python_x - stk_x for (python_x, stk_x) in zip (python_pos_x, stk_pos_x)]
    diff_y = [python_y - stk_y for (python_y, stk_y) in zip (python_pos_y, stk_pos_y)]
    diff_z = [python_z - stk_z for (python_z, stk_z) in zip (python_pos_z, stk_pos_z)]

    plt.plot(times, diff_x, label = 'X Difference')
    plt.plot(times, diff_y, label = 'Y Difference')
    plt.plot(times, diff_z, label = 'Z Difference')
    plt.show()