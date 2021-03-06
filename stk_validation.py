import numpy as np
from helper_functions import get_epoch_time

def get_stk_data(reference_frame):
     stk_data = []


def load_stk_ephemeris(filename):
    stk_data = {}

    ephemeris_list = []

    with open(filename, 'r') as stream:
        data_counter = 0
        data_flag = False

        for count, line in enumerate(stream):
            if 'NumberOfEphemerisPoints' in line:
                data = list(filter(None, line.split(' ')))
                numPoints = int(data[1])
                stk_data['number_points'] = numPoints
            
            if 'CoordinateSystem' in line:
                data = list(filter(None, line.split(' ')))
                coordinate_system = data[1].strip()
                stk_data['coordinate_system'] = coordinate_system
            
            if 'Epoch in YYDDD format' in line:
                data = list(filter(None, line.split(':')))
                epoch_time_string = data[1].strip()
                epoch_time = get_epoch_time(epoch_time_string)
                stk_data['epoch_time'] = epoch_time
            
            if count == 26:
                data_flag = True
                
            if not line:
                print (count)
                data_flag = False
                
            if data_flag and (data_counter < numPoints):
                data_counter += 1
                data = list(filter(None, line.split(" ")))
                time = float(data[0])
                position = np.array([float(data[1]), float(data[2]), float(data[3])])
                ephemeris= {'time' : time, 'position' : position}
                ephemeris_list.append(ephemeris)

    stk_data['ephemeris_list'] = ephemeris_list

    return stk_data