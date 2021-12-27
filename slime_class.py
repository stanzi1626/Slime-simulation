class slime():
    
    def __init__(self, initial_position, x_velocity, y_velocity):
        self.x_position = initial_position[0]
        self.y_position = initial_position[1]
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
        self.trail_xdata = []
        self.trail_ydata = []
    
    def update(self, time_step):
        self.x_position += self.x_velocity * time_step
        self.y_position += self.y_velocity * time_step
        if self.x_position <= 0 or self.x_position >= 1000:
            self.x_velocity = -self.x_velocity
        elif self.y_position <= 0 or self.y_position >= 1000:
            self.y_velocity = -self.y_velocity
    
        return self.x_position, self.y_position
    
    def trail(self):
        self.trail_xdata.append(self.x_position)
        self.trail_ydata.append(self.y_position)
        if len(self.trail_xdata) > 10:
            self.trail_xdata.pop(0)
            self.trail_ydata.pop(0)
        
        return self.trail_xdata, self.trail_ydata
