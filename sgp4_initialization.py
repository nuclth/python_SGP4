import math
from constants import ke, k2
from orbital_relations import get_dimless_semi_parameter, compute_semimajor_axis

def compute_brouwer_mean_motion(kozai_mean_motion, inclination, eccentricity):
    
    n0 = kozai_mean_motion
    i0 = inclination
    e0 = eccentricity

    incl_arg = 3. * math.cos(i0) * math.cos(i0) - 1.
    p = get_dimless_semi_parameter(e0)

    a1 = math.pow((ke / n0), 2./3.)

    d1 = (3./2.) * k2 / (a1 * a1) * incl_arg / math.pow(p, 3.)

    a2 = (1. - (1./3.)*d1 - d1*d1 - (134./81.)*d1*d1*d1)
    d0 = (3./2.) * k2 / (a2 * a2) * incl_arg / math.pow(p, 3.)

    brouwer_mean_motion = n0 / (1. + d0)

    brouwer_semimajor_axis = compute_semimajor_axis(brouwer_mean_motion)

    return (brouwer_mean_motion, brouwer_semimajor_axis)