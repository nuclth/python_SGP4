import math
from constants import k2, q0, rEarth, A30

def get_s_altitude_parameter(perigee_height):
    if (perigee_height < 98):
        s = 20 + rEarth
    elif (perigee_height >= 98) and (perigee_height < 156):
        s = (perigee_height - 78) + rEarth
    else:
        s = 78 + rEarth
    s_norm = s / rEarth
    return s_norm

def get_xi(a, perigee_height):
    s = get_s_altitude_parameter(perigee_height)
    xi = 1. / (a - s)
    return xi

def get_eta(a, e, perigee_height):
    xi = get_xi(a, perigee_height)
    eta = a * e * xi 
    return eta

def get_C1(bstar, perigee_height, a, e, n, t):
    C1 = bstar * get_C2(perigee_height, a, e, n, t)
    return C1

def get_C2(perigee_height, a, e, n, t):
    s = get_s_altitude_parameter(perigee_height)
    xi = get_xi(a, perigee_height)
    eta = get_eta(a, e, perigee_height)  
    prefactor = math.pow(q0 - s, 4.) * math.pow(xi, 4.) * n * math.pow(1 - eta * eta, -7./2.)
    term1 = a * (1. + (3./2.) * math.pow(eta, 2.) + 4. * e * eta + e * math.pow(eta, 3.))
    term2 = (3./2.) * k2 * xi / (1. - eta * eta) * ((3./2.)*t*t - (1./2.)) * (8. + 24. * math.pow(eta, 2.) + 3. * math.pow(eta, 4.))
    C2 = prefactor * (term1 + term2)
    return C2

def get_C3(perigee_height, a, n, i , e):
    s = get_s_altitude_parameter(perigee_height)
    xi = get_xi(a, perigee_height)
    numer = math.pow(q0 - s, 4.) * math.pow(xi, 5.) * A30 * n * math.sin(i)
    denom = k2 * e
    C3 = numer / denom
    return C3

def get_C4(perigee_height, a, e, n, p, t, w):
    s = get_s_altitude_parameter(perigee_height)
    xi = get_xi(a, perigee_height)
    eta = get_eta(a, e, perigee_height)
    prefactor1 = 2. * n * math.pow(q0 - s, 4.) * math.pow(xi, 4.) * a * math.pow(p, 2.) * math.pow(1. - eta*eta, -7./2.)
    prefactor2 = 2. * k2 * xi / (a * (1. - eta*eta))
    term1 = 2. * eta * (1. + e * eta) + (1./2.) * e + (1./2.) * math.pow(eta, 3.)
    term2 = 3. * (1. - 3. * t*t) * (1. + (3./2.)*eta*eta - 2.* e * eta - (1./2.) * e * math.pow(eta, 3.))
    term3 = (3./4.) * (1. - t*t) * (2. * eta * eta - e * eta - e * math.pow(eta, 3.)) * math.cos(2.*w)

    C4 = prefactor1 * (term1 - prefactor2 * (term2 + term3))
    return C4

def get_C5(perigee_height, a, e, p):
    s = get_s_altitude_parameter(perigee_height)
    xi = get_xi(a, perigee_height)
    eta = get_eta(a, e, perigee_height)
    prefactor = 2. * math.pow(q0 - s, 4.) * math.pow(xi, 4.) * a * math.pow(p, 2.) * math.pow(1. - eta*eta, -7./2.)
    brackets = 1. + (11./4.) * eta * (eta + e) + e * math.pow(eta, 3.)
    C5 = prefactor * brackets
    return C5

def get_D2(bstar, perigee_height, a, e, n, t):
    C1 = get_C1(bstar, perigee_height, a, e, n, t)
    xi = get_xi(a, perigee_height)
    D2 = 4. * a * xi * math.pow(C1, 2.)
    return D2

def get_D3(bstar, perigee_height, a, e, n, t):
    C1 = get_C1(bstar, perigee_height, a, e, n, t)
    xi = get_xi(a, perigee_height)
    s = get_s_altitude_parameter(perigee_height)
    D3 = (4./3.) * a * math.pow(xi, 2.) * (17.*a + s) * math.pow(C1, 3.)
    return D3

def get_D4(bstar, perigee_height, a, e, n, t):
    s = get_s_altitude_parameter(perigee_height)
    xi = get_xi(a, perigee_height)
    C1 = get_C1(bstar, perigee_height, a, e, n, t)
    D4 = (2./3.) * math.pow(a, 2.) * math.pow(xi, 3.) * math.pow(C1, 4.) * (221. * a + 31. * s)
    return D4