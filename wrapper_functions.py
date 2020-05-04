import math
import datetime
from constants import rEarth
from tle_parsing import parse_tle_file
from orbital_relations import compute_perigee_height, get_dimless_semi_parameter
from sgp4_initialization import compute_brouwer_mean_motion
from updates import zonal_harmonic_atmospheric_update, secondary_atmospheric_update_wrapper
from long_periodic_gravity_updates import long_periodic_gravity_update
from kepler_equation import kepler_iteration
from short_periodic_gravity_updates import short_periodic_gravity_update

def validate_sgp4(filename):
    tle_objs = parse_tle_file(filename)
    time_start = datetime.datetime(2020, 4, 30, 16, 0, 0, 0)

    time_vals = [time_start + datetime.timedelta(seconds=t) for t in range(0,10)]

    for tle_obj in tle_objs:

        fileout = tle_obj['catalog_string'] + '_pos.txt'
        
        print("WARNING: BSTAR SET TO 0")
        tle_obj['bstar'] = 0.

        with open(fileout, 'w') as stream:

            for time_val in time_vals:
                
                pos = sgp4(tle_obj, time_val)
                pos *= rEarth

                time_string = time_val.strftime("%m/%d/%Y-%H:%M:%S")
                pos_string = "%s, %7f, %7f, %7f\n" % (time_string, pos[0], pos[1], pos[2])
                stream.write(pos_string)
            
            stream.close

def sgp4(tle_obj, time_val):

    # step 0 - get variables
    kozai_n = tle_obj['mean_motion']
    i0 = tle_obj['inclination']
    e0 = tle_obj['eccentricity']
    bstar = tle_obj['bstar']
    m0 = tle_obj['mean_anomaly']
    w0 = tle_obj['arg_perigee']
    o0 = tle_obj['raan']
    time_diff = compute_time_diff(tle_obj['epoch_time'], time_val)

    # step 1 - convert mean motion from kozai to brouwer
    (n0, a0) = compute_brouwer_mean_motion(kozai_n, i0, e0)

    h = compute_perigee_height(a0, e0)

    # step 2 - update for zonal harmonics and atmospheric effects
    (m, w, o) = zonal_harmonic_atmospheric_update(bstar, m0, w0, o0, i0, e0, a0, n0, time_diff, h)

    # step 3 - update for more atmospheric effects
    p0 = get_dimless_semi_parameter(e0)
    t = math.cos(i0)
    n = n0 # TODO add earth resonance effects
    (e, a, IL) = secondary_atmospheric_update_wrapper(h, a0, e0, n, n0, p0, t, w0, bstar, time_diff, m, m0, o0)
    
    # step 4 - update for long periodic effects of earth gravity
    p = get_dimless_semi_parameter(e)
    (axN, ayN, ILT) = long_periodic_gravity_update(e, w, i0, a, p, IL)

    # step 5 - solve kepler equation
    E_plus_w = kepler_iteration(ILT, o, axN, ayN)

    # step 6 - update for short periodic effects of earth gravity
    pos = short_periodic_gravity_update(axN, ayN, E_plus_w, a, i0, o)

    return pos

def compute_time_diff(epoch_time, time_val):
    tdiff = time_val - epoch_time
    time_mins = (tdiff.days * 24 * 60) + (tdiff.seconds / 60.)
    return time_mins