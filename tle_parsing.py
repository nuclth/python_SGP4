import math
import datetime
from constants import DEGREES_TO_RADIANS

def parse_tle_file(filename):

    tle_objs = []

    with open(filename, 'r') as stream:

        line_1 = ''
        line_2 = ''

        for line in stream:

            if(line[0] == '1'):
                line_1 = line
            elif(line[0] == '2'):
                line_2 = line

            if (line_1 and line_2):
                tle_obj = parse_tle(line_1, line_2)
                tle_objs.append(tle_obj)
                line_1 = ''
                line_2 = ''

        stream.close()

    return tle_objs


def parse_tle(line_1, line_2):

    if (len(line_1) is not 69) or (len(line_2) is not 69):
        SystemExit

    if (line_1[0] != '1') or (line_2[0] != '2'):
        SystemExit

    tle_obj = {}
    tle_obj['line_1'] = line_1
    tle_obj['line_2'] = line_2
    
    (catalog_string, epoch_time, bstar) = parse_tle_line_1(line_1)
    
    tle_obj['catalog_string'] = catalog_string
    tle_obj['epoch_time'] = epoch_time
    tle_obj['bstar'] = bstar

    (inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion) = parse_tle_line_2(line_2)

    tle_obj['inclination'] = inclination
    tle_obj['raan'] = raan
    tle_obj['eccentricity'] = eccentricity
    tle_obj['arg_perigee'] = arg_perigee
    tle_obj['mean_anomaly'] = mean_anomaly
    tle_obj['mean_motion'] = mean_motion

    return tle_obj

def parse_tle_line_1(line):

    catalog_string = line[2:7]
    bstar_term = '0.' + line[54:61]

    if '-' in bstar_term:
        bstar_lead = float(bstar_term.split('-')[0])
        bstar_exp = -1. * float(bstar_term.split('-')[1])
    elif '+' in bstar_term:
        bstar_lead = float(bstar_term.split('+')[0])
        bstar_exp = float(bstar_term.split('+')[1])

    bstar = bstar_lead * 10.**bstar_exp

    year = 2000 + int(line[18:20]) if int(line[18:20]) < 30 else 1900 + int(line[18:20])
    doy = int(line[20:23])
    day_frac = float(line[23:32])
    month = (datetime.datetime(year,1,1) + datetime.timedelta(days=doy-1)).month
    day = (datetime.datetime(year,1,1) + datetime.timedelta(days=doy-1)).day
    hour = math.floor(day_frac * 24.)
    minute = math.floor((day_frac * 24 * 60) % 60)
    second = math.floor((day_frac * 24 * 3600) % 60)

    epoch_time = datetime.datetime(year, month, day, hour, minute, second)

    return (catalog_string, epoch_time, bstar)
    
def parse_tle_line_2(line):
    inclination = float(line[8:16]) * DEGREES_TO_RADIANS 
    raan = float(line[17:25]) * DEGREES_TO_RADIANS 
    eccentricity = float('0.' + line[26:33])
    arg_perigee = float(line[34:42]) * DEGREES_TO_RADIANS
    mean_anomaly = float(line[43:51]) * DEGREES_TO_RADIANS 
    mean_motion = float(line[52:63]) / 1440. #TODO check units, revs/day initially -> revs/min

    return (inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion)
