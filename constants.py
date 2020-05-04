import math

## value given constants

DEGREES_TO_RADIANS = math.pi / 180.

# universal gravitational constants
G = 6.67430 * 1.0e-11 * 1.0e-9 # TODO get real value

# mass of the earth in kg
M = 5.9722 * 1.0e24 

# J2 value 
J2 = 1.082616 * 1.0e-3

# J3 value
J3 = -0.253881 * 1.0e-5

# J4 value
J4 = -1.65597 * 1.0e-6

# equatorial earth radius in km
rEarth = 6378.137 

## Constants defined via equations

# 
ke = 0.0743669161# TODO FIX THIS to be math.sqrt(G*M) in correct units

#
k2 = (1./2.) * J2 #* math.pow(rEarth, 2.)

# 
k4 = (-3./8.) * J4 #* math.pow(rEarth, 4.)

# atmospheric altitude parameter
q0 = (120 + rEarth) / rEarth

# atmospheric coefficient
A30 = -J3# * math.pow(rEarth, 3.)