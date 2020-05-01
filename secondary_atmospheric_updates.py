import math
from constants import ke
from atmospheric_variables import get_C1, get_C4, get_C5, get_D2, get_D3, get_D4

def secondary_atmospheric_update(perigee_height, a, e, n, n0, p, t, w, bstar, time_diff, m, m0):

    # TODO Fix this with consideration of earth resonance effects

    delta_e = compute_delta_e(perigee_height, a, e, n, p, t, w, bstar, time_diff, m, m0)
    delta_a = compute_delta_a(bstar, perigee_height, a, e, n, n0, t, time_diff)
    delta_IL = compute_delta_IL(bstar, perigee_height, a, e, n0, t, time_diff)

    return (delta_e, delta_a, delta_IL)

def compute_delta_e(perigee_height, a, e, n, p, t, w, bstar, time_diff, m, m0):
    C4 = get_C4(perigee_height, a, e, n, p, t, w)
    C5 = get_C5(perigee_height, a, e, p)

    delta_e = bstar * C4 * time_diff + bstar * C5 * (math.sin(m) - math.sin(m0))

    return delta_e

def compute_delta_a(bstar, perigee_height, a, e, n, n0, t, time_diff):
    C1 = get_C1(bstar, perigee_height, a, e, n0, t)
    D2 = get_D2(bstar, perigee_height, a, e, n0, t)
    D3 = get_D3(bstar, perigee_height, a, e, n0, t)
    D4 = get_D4(bstar, perigee_height, a, e, n0, t)

    prefactor = math.pow(ke / n, 2./3.) 
    brackets = 1. - C1 * time_diff - D2 * math.pow(time_diff, 2.) - D3 * math.pow(time_diff, 3.) - D4 * math.pow(time_diff, 4.)

    delta_a = prefactor * math.pow(brackets, 2.)

    return delta_a

def compute_delta_IL(bstar, perigee_height, a, e, n, t, time_diff):
    C1 = get_C1(bstar, perigee_height, a, e, n, t)
    D2 = get_D2(bstar, perigee_height, a, e, n, t)
    D3 = get_D3(bstar, perigee_height, a, e, n, t)
    D4 = get_D4(bstar, perigee_height, a, e, n, t)

    term1 = (3./2.) * C1 * math.pow(time_diff, 2.)
    term2 = (D2 + 2. * math.pow(C1, 2.))* math.pow(time_diff, 3.)
    term3 = (1./4.) * (3.*D3 + 12.*C1*D2 + 10.*math.pow(C1, 3.)) * math.pow(time_diff, 4.)
    term4 = (1./5.) * (3.*D4 + 12.*C1*D3 + 6.*math.pow(D2,2.) + 30.*math.pow(C1,2.)*D2 + 15.*math.pow(C1,4.)) * math.pow(time_diff, 5.)

    delta_IL = n * (term1 + term2 + term3 + term4)
    
    return delta_IL