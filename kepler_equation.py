import math
import sys

def kepler_iteration(ILT, omega, axN, ayN):
    U = ILT - omega

    E_plus_w_0 = U

    delta_E_plus_w = compute_kepler_delta_equation(U, axN, ayN, E_plus_w_0)

    prev_E_plus_w = E_plus_w_0
    E_plus_w = E_plus_w_0 + delta_E_plus_w

    percent_diff = get_percent_diff(prev_E_plus_w, E_plus_w)

    while(percent_diff > 1):
        prev_E_plus_w = E_plus_w
        delta_E_plus_w = compute_kepler_delta_equation(U, axN, ayN, prev_E_plus_w)
        E_plus_w = prev_E_plus_w + delta_E_plus_w
        percent_diff = get_percent_diff(prev_E_plus_w, E_plus_w)

    return E_plus_w


def compute_kepler_delta_equation(U, axN, ayN, E_plus_w):
    
    numer = U - ayN * math.cos(E_plus_w) + axN * math.sin(E_plus_w) - E_plus_w
    denom = 1. - ayN * math.sin(E_plus_w) - axN * math.cos(E_plus_w)

    delta_E_plus_w = numer / denom

    return delta_E_plus_w

def get_percent_diff(prev, next):

    if next == 0:
        print("Error: Denominator is zero in percent difference")
        sys.exit(1)

    percent_diff = 100. * (next - prev) / next

    return percent_diff