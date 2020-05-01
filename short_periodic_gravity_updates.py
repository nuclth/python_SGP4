import math

def eTrigE(axN, ayN, E_plus_w):

    eCosE = axN * math.cos(E_plus_w) + ayN * math.sin(E_plus_w)
    eSinE = axN * math.sin(E_plus_w) - ayN * math.cos(E_plus_w)

    return (eCosE, eSinE)

