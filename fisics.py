class fisics:
    def __init__(self, position ,mass=0,acceleration_x=0,acceleration_y=0,radios=0):
        self.x = position[0]
        self.y = position[1]
        self.mass = mass
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.limit = False
        self.radios = radios
    def set_limit(self,limit,width,height):
        self.limit = limit
        self.width = width
        self.height = height
    
    def get_force_x(self):
        self.x += self.mass * self.acceleration_x
    def get_force_y(self):
        self.y += self.mass * self.acceleration_y
    def set_move_x(self):
        if not self.limit:
            self.x += self.acceleration_x
        else:
            limit = self.width - self.limit
            if limit <= 0: 
                self.x = limit
    def set_move_y(self):
        if not self.limit:
            self.y += self.acceleration_y
        else:
            limit = self.height - self.limit
            if limit <= 0: 
                self.x = limit
    def update(self):
        return self.x, self.y