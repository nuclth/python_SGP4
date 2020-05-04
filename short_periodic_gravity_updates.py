import math
from orientation_vectors import U_vector
from orbital_relations import get_semi_parameter
from constants import ke, k2

def eTrigE(axN, ayN, E_plus_w):

    eCosE = axN * math.cos(E_plus_w) + ayN * math.sin(E_plus_w)
    eSinE = axN * math.sin(E_plus_w) - ayN * math.cos(E_plus_w)

    return (eCosE, eSinE)

def compute_eccentricity(axN, ayN):
    return math.sqrt(axN*axN + ayN*ayN)

def get_r(a, eCosE):
    return a* (1. - eCosE)

def compute_rdot(a, r, eSinE):
    rdot = ke * math.sqrt(a) /r * eSinE
    return rdot

def compute_pl(a, e):
    return a * (1. - e*e)

def compute_rfdot(e, a, r):
    pl = compute_pl(a, e)
    rfdot = ke * math.sqrt(pl) / r
    return rfdot

def compute_cosu(a, r, E_plus_w, axN, ayN, e, eSinE):
    term1 = math.cos(E_plus_w) - axN
    term2 = ayN * eSinE / (1. + math.sqrt(1. - e*e))
    return (a/r) * (term1 + term2)

def compute_sinu(a, r, E_plus_w, axN, ayN, e, eSinE):
    term1 = math.sin(E_plus_w) - ayN
    term2 = axN * eSinE / (1. + math.sqrt(1. - e*e))
    return (a/r) * (term1 - term2)

def compute_u(a, r, E_plus_w, axN, ayN, e, eSinE):
    sinu = compute_sinu(a, r, E_plus_w, axN, ayN, e, eSinE)
    cosu = compute_cosu(a, r, E_plus_w, axN, ayN, e, eSinE)
    return math.atan2(sinu, cosu)

def compute_delta_r(a, e, i, u):
    pl = compute_pl(a, e)
    delta_r = k2 / (2. * pl) * (1. - math.cos(i) * math.cos(i)) * math.cos(2. * u)
    return delta_r

def compute_delta_u(a, e, i, u):
    pl = compute_pl(a, e)
    delta_u = -k2 / (4. * pl * pl) * (7. * math.cos(i) * math.cos(i) - 1.) * math.sin(2. * u)
    return delta_u

def compute_delta_o(a, e, i, u):
    pl = compute_pl(a, e)
    delta_o = 3. * k2 * math.cos(i) * math.sin(2. * u) / (2. * pl * pl)
    return delta_o

def compute_delta_i(a, e, i, u):
    pl = compute_pl(a, e)
    delta_i = 3. * k2 * math.cos(i) * math.sin(i) * math.cos(2. * u) / (2. * pl * pl)
    return delta_i

def compute_delta_rdot(a, e, i, u, n):
    pl = compute_pl(a, e)
    delta_rdot = - k2 * n / pl * (1. - math.cos(i) * math.cos(i)) * math. sin(2. * u)
    return delta_rdot

def update_rk(a, e, r, i, u):
    pl = compute_pl(a, e)
    term1 = r * (1. - (3./2.) * k2 * math.sqrt(1. - e * e) * (3. * math.cos(i) * math.cos(i) - 1.) / (pl * pl))
    delta_r = compute_delta_r(a, e, i, u)
    return term1 + delta_r

def update_uk(a, e, i, u):
    delta_u = compute_delta_u(a, e, i ,u)
    return u + delta_u

def update_ok(a, e, i, u, o):
    delta_o = compute_delta_o(a, e, i, u)
    return o + delta_o

def update_ik(a, e, i, u):
    delta_i = compute_delta_i(a, e, i, u)
    return i + delta_i

def update_rdotk(a, e, i, u, n, rdot):
    delta_rdot = compute_delta_rdot(a, e, i, u, n)
    return rdot + delta_rdot

def compute_position(a, e, r, i ,u, o):
    rk = update_rk(a, e, r, i, u)
    uk = update_uk(a, e, i, u)
    ok = update_ok(a, e, i, u, o)
    ik = update_ik(a, e, i, u)
    Uvec = U_vector(uk, ok, ik)
    r = rk * Uvec
    return r

def short_periodic_gravity_update(axN, ayN, E_plus_w, a, i, o):
    e = compute_eccentricity(axN, ayN)
    (eCosE, eSinE) = eTrigE(axN, ayN, E_plus_w)
    r = get_r(a, eCosE)
    u = compute_u(a, r, E_plus_w, axN, ayN, e, eSinE)

    pos = compute_position(a, e, r, i, u, o)
    return pos