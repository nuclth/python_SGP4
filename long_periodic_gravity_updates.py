import math 
from constants import A30, k2

def long_periodic_gravity_update(e, w, i, a, p, IL):

    axN = e * math.cos(w)

    ayNL = A30 * math.sin(i) / (4. * k2 * a * p * p)
    ayN = e * math.sin(w) + ayNL

    ILL = A30 * math.sin(i) / (8. * k2 * a * p * p) * (e * math.cos(w)) * ((3. + 5.*math.cos(i))/ (1. + math.cos(i)))
    ILT = IL + ILL

    return (axN, ayN, ILT)