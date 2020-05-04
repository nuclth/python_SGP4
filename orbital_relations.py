import math
from constants import rEarth, ke

def get_dimless_semi_parameter(e):
    return math.sqrt(1 - e*e)

def get_semi_parameter(e, a):
    return (a * get_dimless_semi_parameter(e))

def compute_perigee_height(a, e):
    perigee_height = rEarth * (a * (1. - e) - 1.)
    #perigee_height = a * (1 - e) - rEarth
    #perigee_height = a * (1. - e) - 1.
    return perigee_height

def compute_semimajor_axis(n):
    return math.pow(ke / (2. * math.pi * n), (2./3.))