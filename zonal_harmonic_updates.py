import math
from constants import k2, k4
from orbital_relations import get_dimless_semi_parameter

def zonal_harmonic_update(inclination, eccentricity, semimajor_axis, mean_motion):

    mean_anomaly = zonal_mean_anomaly_update(inclination, eccentricity, semimajor_axis, mean_motion)
    arg_perigee = zonal_arg_perigee_update(inclination, eccentricity, semimajor_axis, mean_motion)
    raan = zonal_raan_update(inclination, eccentricity, semimajor_axis, mean_motion)

    return (mean_anomaly, arg_perigee, raan)

def zonal_mean_anomaly_update(inclination, eccentricity, semimajor_axis, mean_motion):
    
    a = semimajor_axis
    p = get_dimless_semi_parameter(eccentricity)
    theta = math.cos(inclination)

    term1 = compute_k2_mean_anomaly(a, p, theta)
    term2 = compute_k2_square_mean_anomaly(a, p, theta)

    update = (term1 + term2) * mean_motion
    return update
    

def zonal_arg_perigee_update(inclination, eccentricity, semimajor_axis, mean_motion):
    a = semimajor_axis
    p = get_dimless_semi_parameter(eccentricity)
    theta = math.cos(inclination)

    term1 = compute_k2_arg_perigiee(a, p, theta)
    term2 = compute_k2_square_arg_perigiee(a, p, theta)
    term3 = compute_k4_arg_perigiee(a, p, theta)

    update = (term1 + term2 + term3) * mean_motion
    return update

def zonal_raan_update(inclination, eccentricity, semimajor_axis, mean_motion):
    a = semimajor_axis
    p = get_dimless_semi_parameter(eccentricity)
    theta = math.cos(inclination)

    term1 = compute_k2_raan(a, p, theta)
    term2 = compute_k2_square_raan(a, p, theta)
    term3 = compute_k4_raan(a, p, theta)

    update = (term1 + term2 + term3) * mean_motion
    return update

def compute_k2_mean_anomaly(a, p, t):
    numer = 3. * k2 * (3. * math.pow(t, 2.) - 1.)
    denom = 2. * math.pow(a, 2.) * math.pow(p, 3.)
    term = numer / denom
    return term
    
def compute_k2_square_mean_anomaly(a, p, t):
    numer = 3. * math.pow(k2, 2.) * (7. - 114. * math.pow(t, 2.) + 137. * math.pow(t, 4.))
    denom = 16. * math.pow(a, 4.) * math.pow(p, 7.) 
    term = numer / denom
    return term

def compute_k2_arg_perigiee(a,p,t):
    numer = -3. * k2 * (1 - 5. * math.pow(t, 2.))
    denom = 2. * math.pow(a, 2.) * math.pow(p, 4.)
    term = numer / denom
    return term

def compute_k2_square_arg_perigiee(a,p,t):
    numer = 3. * math.pow(k2, 2.) * (7. - 114. * math.pow(t, 2.) + 395. * math.pow(t, 4.))
    denom = 16. * math.pow(a, 4.) * math.pow(p, 8.)
    term = numer / denom
    return term

def compute_k4_arg_perigiee(a,p,t):
    numer = 5. * k4 * (3. - 36. * math.pow(t, 2.) + 49. * math.pow(t, 4.))
    denom = 4. * math.pow(a, 4.) * math.pow(p, 8.)
    term = numer / denom
    return term

def compute_k2_raan(a,p,t):
    numer = -3. * k2 * t
    denom = math.pow(a, 2.) * math.pow(p, 4.)
    term = numer / denom
    return term

def compute_k2_square_raan(a,p,t):
    numer = 3. * math.pow(k2, 2.) * (4.*t - 19. * math.pow(t, 3.))
    denom = 2. * math.pow(a, 4.) * math.pow(p, 8.)
    term = numer / denom
    return term

def compute_k4_raan(a,p,t):
    numer = 5. * k4 * t * (3. - 7. * math.pow(t, 2.))
    denom = 2. * math.pow(a, 4.) * math.pow(p, 8.)
    term = numer / denom
    return term
