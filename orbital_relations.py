import math
from constants import rEarth

def get_dimless_semi_parameter(e):
    return math.sqrt(1 - e*e)

def get_semi_parameter(e, a):
    return (a * get_dimless_semi_parameter(e))

def compute_perigee_height(a, e):
    perigee_height = a * (1 - e) - rEarth
    return perigee_height