import math
import numpy as np

def rot3(arg):
    return np.matrix([[math.cos(arg), math.sin(arg), 0], [-math.sin(arg), math.cos(arg), 0], [0, 0, 1]])

def jd2tut1(jd):
    return ((jd - 2451545.0) / 36525.)

def tut12gmst(tut1):
    gmst = math.pi/(180.*240.) * (67310.54841 + ((876600.*3600.) + 8640184.812866) * tut1 + 0.093104 * tut1*tut1 - 6.2e-6 * tut1*tut1*tut1)
    return gmst

def teme2pef(pos_teme, time):
    gmst = epoch2gmst(time)
    rot_matrix = rot3(gmst)
    temp_pos_pef = np.matmul(rot_matrix, pos_teme) # TODO make this and next step more elegant
    pos_pef = np.array([temp_pos_pef[0,0], temp_pos_pef[0,1], temp_pos_pef[0,2]])
    return pos_pef

def epoch2jd(year, mo, d, h, mins, s):
    jd = 367. * year - math.floor(7.*(year + math.floor((mo+9.)/12.))/4.) + math.floor(275. * mo / 9.) + d + 1721013.5 + ((((s/60.) + mins)/60.) + h) / 24.
    return jd

def epoch2gmst(time):
    jd = epoch2jd(time.year, time.month, time.day, time.hour, time.minute, time.second)
    tut1 = jd2tut1(jd)
    gmst = tut12gmst(tut1)
    return gmst