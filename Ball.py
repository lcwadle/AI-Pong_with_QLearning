class Ball:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.x_velocity = velocity_x
        self.y_velocity = velocity_y
        self.missed = False
