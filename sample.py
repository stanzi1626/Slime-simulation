import math
from random import choices

def sample(x_position, y_position, x_velocity, y_velocity, trail_data):
    #initial idea is to sum the intensities: left (-1), center (0), right (1)and to randomly choose between the 3 weighted on their total intensity
    #the sample is taken as a sector in front of the slime, with each sector 30 degrees
    
    theta = math.pi / 6 #30 degrees
    sample_range = 50

    centre_intensity = 0
    left_intensity = 0
    right_intensity = 0

    direction = 10

    for line in trail_data:
        x_relative_vector = -(x_position - line[0][0])
        y_relative_vector = -(y_position - line[0][1])

        relative_vector_amplitude = math.sqrt(x_relative_vector**2 + y_relative_vector**2)
        velocity_amplitude = math.sqrt(x_velocity**2 + y_velocity**2)

        dot_product = (x_relative_vector*x_velocity + y_relative_vector*y_velocity) / (relative_vector_amplitude*velocity_amplitude)
        if dot_product > 1:
            dot_product = 1
        elif dot_product < -1:
            dot_product = -1

        sample_theta = math.acos(dot_product)
        
        if sample_theta > math.pi:
            sample_theta = 2*math.pi - sample_theta
        #check whether trail is within sample region
        if sample_theta > 3/2*theta or sample_theta < -3/2*theta or relative_vector_amplitude > sample_range:
            continue

        #check which of the sample regions the trail is within
        #central region
        if sample_theta > -theta/2 and sample_theta < theta/2:
            centre_intensity += line[1] * (1 / relative_vector_amplitude) #trails further away will have less of an influence
        #left region
        elif sample_theta < -theta/2:
            left_intensity += line[1] * (1 / relative_vector_amplitude)
        #right region
        elif sample_theta > theta/2:
            right_intensity += line[1] * (1 / relative_vector_amplitude)
        
    if left_intensity + right_intensity + centre_intensity != 0:
        factor = left_intensity + right_intensity + centre_intensity
        if left_intensity != 0:
            left_propability = left_intensity / factor
        else:
            left_propability = 0
        if right_intensity != 0:
            right_propability = right_intensity / factor
        else:
            right_propability = 0
        if centre_intensity != 0:
            centre_propability = centre_intensity / factor
        else:
            centre_propability = 0
        #return -1, 0 or 1 weighted on the intensity
        direction = choices([-1, 0, 1], weights = [left_propability, centre_propability, right_propability], k=1)[0]
    
    if left_intensity + right_intensity + centre_intensity == 0:
        direction = 0
        
    if direction != 0:
        print("WOOOO")

    return direction
    