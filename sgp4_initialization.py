import math
import datetime
from constants import ke, DEGREES_TO_RADIANS
from orbital_relations import get_dimless_semi_parameter

def parse_tle(line_1, line_2):
    # TODO set this up

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
    raw_time = line[18:32]
    bstar = float(line[53:61])

    year = 2000 + float(raw_time[0:2]) if float(raw_time[0:2]) < 30 else 1900 + float(raw_time[0:2])
    doy = line[20:23]
    month = (datetime.datetime(year,1,1) - datetime.timedelta(days=doy-1)).month
    day = (datetime.datetime(year,1,1) - datetime.timedelta(days=doy-1)).day
    hour = 
    minute = 
    second = 

    epoch_time = datetime.datetime(year, month, day, hour, minute, second)

    return (catalog_string, epoch_time, bstar)
    
def parse_tle_line_2(line):
    inclination = float(line[8:16]) * DEGREES_TO_RADIANS 
    raan = float(line[17:25]) * DEGREES_TO_RADIANS 
    eccentricity = string_eccentricity_to_num(line[26:32]) #TODO fix decimal point
    arg_perigee = float(line[34:42]) * DEGREES_TO_RADIANS
    mean_anomaly = float(line[43:51]) * DEGREES_TO_RADIANS 
    mean_motion = float(line[52:63]) / 1440. #TODO check units, revs/day initially -> revs/min

    return (inclination, raan, eccentricity, arg_perigee, mean_anomaly, mean_motion)

def string_eccentricity_to_num(string_fragment):
    pass

def compute_brouwer_mean_motion(kozai_mean_motion, inclination, eccentricity, k2):
    
    n0 = kozai_mean_motion
    i0 = inclination
    e0 = eccentricity

    incl_arg = 3. * math.cos*(i0) * math.cos(i0) - 1.
    p = get_dimless_semi_parameter(e0)

    a1 = math.pow((ke / n0), 2./3.)
    d1 = (3./2.) * k2 / (a1 * a1) * incl_arg / math.pow(p, 3.)

    a2 = (1. - (1./3.)*d1 - d1*d1 - (134./81.)*d1*d1*d1)
    d0 = (3./2.) * k2 / (a2 * a2) * incl_arg / math.pow(p, 3.)

    brouwer_mean_motion = n0 / (1. + d0)
    brouwer_semimajor_axis = math.pow((ke / brouwer_mean_motion), 2./3.)

    return (brouwer_mean_motion, brouwer_semimajor_axis)

