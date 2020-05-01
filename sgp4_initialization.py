import math
from constants import ke
from orbital_relations import get_dimless_semi_parameter

def parse_tle(tleFile):
    # TODO set this up
    pass
    epoch_time = 0
    mean_motion = 0
    eccentricity = 0 
    inclination = 0 
    arg_of_perigee = 0 
    raan = 0
    mean_anomaly = 0 
    bstar = 0 

    return (epoch_time, mean_motion, eccentricity, inclination, arg_of_perigee, raan, mean_anomaly, bstar)

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

