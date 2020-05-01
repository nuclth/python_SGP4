from zonal_harmonic_updates import zonal_harmonic_update
from primary_atmospheric_updates import primary_atmospheric_update

def zonal_harmonic_atmospheric_update(bstar, mean_anomaly, arg_perigee, raan, inclination, eccentricity, semimajor_axis, mean_motion, time_diff):

    (m_zonal, w_zonal, o_zonal) = zonal_harmonic_update(inclination, eccentricity, semimajor_axis, mean_motion)

    M_DF = (mean_anomaly) + (mean_motion * time_diff) + (m_zonal * time_diff)
    W_DF = arg_perigee + (w_zonal * time_diff)
    O_DF = raan + (o_zonal * time_diff)

    (delta_M, delta_W, delta_O) = primary_atmospheric_update(bstar, semimajor_axis, mean_motion, mean_anomaly, inclination, arg_perigee, eccentricity, time_diff, perigee_height, M_DF)

    updated_mean_anomaly = M_DF + delta_W + delta_M
    updated_arg_perigee = W_DF - delta_W - delta_M
    updated_raan = O_DF - delta_O

    return (updated_mean_anomaly, updated_arg_perigee, updated_raan)

def secondary_atmospheric_update():

    (delta_e, delta_a, delta_IL) = secondary_atmospheric_update()

    updated_eccentricity = e - delta_e 
    updated_semimajor_axis = delta_a 
    updated_angular_IL = m + w + o + delta_IL

    return (updated_eccentricity, updated_semimajor_axis, updated_angular_IL)