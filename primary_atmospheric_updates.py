import math
from constants import q0, rEarth, k2
from orbital_relations import get_dimless_semi_parameter
from atmospheric_variables import get_s_altitude_parameter, get_eta, get_xi, get_C3, get_C1

def primary_atmospheric_update(bstar, semimajor_axis, mean_motion, mean_anomaly, inclination, arg_perigee, eccentricity, time_diff, perigee_height, M_DF):

    a = semimajor_axis
    n = mean_motion
    e = eccentricity
    m = mean_anomaly
    i = inclination

    t = math.cos(i)
    p = get_dimless_semi_parameter(e)

    delta_M = compute_delta_M(perigee_height, a, e, bstar, M_DF, m)
    delta_W = compute_delta_W(perigee_height, a, n, i, e, bstar, arg_perigee, time_diff)
    delta_O = compute_delta_O(bstar, perigee_height, a, e, n, t, p, time_diff)

    return (delta_M, delta_W, delta_O)

def compute_delta_M(perigee_height, a, e, bstar, M_DF, m):
    
    s = get_s_altitude_parameter(perigee_height)
    eta = get_eta(a, e, perigee_height)
    xi = get_xi(a, perigee_height)

    prefactor = -(2./3.) * math.pow(q0 - s, 4.) * bstar * math.pow(xi, 4.) / (e * eta) # TODO Verify rEarth not here
    term1 = math.pow(1. + eta * math.cos(M_DF), 3.)
    term2 = math.pow(1. + eta * math.cos(m), 3.)

    delta_M = prefactor * (term1 - term2)
    return delta_M

def compute_delta_W(perigee_height, a, n, i, e, bstar, arg_perigee, time_diff):
    C3 = get_C3(perigee_height, a, n, i , e)
    delta_W = bstar * C3 * math.cos(arg_perigee) * time_diff
    return delta_W

def compute_delta_O(bstar, perigee_height, a, e, n, t, p, time_diff):
    C1 = get_C1(bstar, perigee_height, a, e, n, t)
    delta_O = (21./2.) * n * k2 * t / (math.pow(a, 2.) * math.pow(p, 2.)) * C1 * math.pow(time_diff, 2.)
    return delta_O