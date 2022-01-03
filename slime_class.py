import numpy as np
import math

class slime():
    
    def __init__(self, initial_position, x_velocity, y_velocity):
        self.x_position = initial_position[0]
        self.y_position = initial_position[1]
        self.x_velocity = x_velocity / math.sqrt(x_velocity**2 + y_velocity**2)
        self.y_velocity = y_velocity / math.sqrt(x_velocity**2 + y_velocity**2)

        self.turning_angle = math.pi / 90 #2 degrees

        self.trail_array =np.zeros((0, 3)) #the first position contains the coordinates of the trail while the second position contains the intensity
    
    def update(self, time_step, direction):

        x_velocity_prime = self.x_velocity
        y_velocity_prime = self.y_velocity
        
        #turn left
        if direction == -1:
            self.y_velocity = x_velocity_prime * math.sin(-self.turning_angle) + y_velocity_prime * math.cos(-self.turning_angle)
            self.x_velocity = x_velocity_prime * math.cos(-self.turning_angle) - y_velocity_prime * math.sin(-self.turning_angle)
        #turn right
        if direction == 1:
            self.y_velocity = x_velocity_prime * math.sin(self.turning_angle) + y_velocity_prime * math.cos(self.turning_angle)
            self.x_velocity = x_velocity_prime * math.cos(self.turning_angle) - y_velocity_prime * math.sin(self.turning_angle)

        self.x_position += self.x_velocity * time_step
        self.y_position += self.y_velocity * time_step
        if self.x_position <= 0 or self.x_position >= 1000:
            self.x_velocity = -self.x_velocity
        elif self.y_position <= 0 or self.y_position >= 1000:
            self.y_velocity = -self.y_velocity
    
        return self.x_position, self.y_position
    
    def trail(self, x_previous, y_previous):

        self.trail_array = np.vstack((np.array((x_previous, y_previous, 1.01)), self.trail_array))

        for count, array in enumerate(self.trail_array):
            array[2] -= 0.01
            array[2] = float("{:.2f}".format(array[2]))
            if array[2] <= 0:
                self.trail_array = np.delete(self.trail_array, count, axis=0)
        
        return self.trail_array
