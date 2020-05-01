import math

def get_dimless_semi_parameter(e):
    return math.sqrt(1 - e*e)

def get_semi_parameter(e, a):
    return (a * get_dimless_semi_parameter(e))
