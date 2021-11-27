class Extruder:
    
    def __init__(self, stalling_prob):
        self.stalling_prob = stalling_prob
        
        self.active = True
        self.left = True
        self.right = True
        self.bind = False
        
        self.current_left = None
        self.current_right = None
        
    def set_direction(self, index, direction):
        if self.left and direction == "left":
            self.current_left = index
        elif self.right and direction == "right":
            self.current_right = index

    def set_direction_status(self, boolean, direction):
        if direction == "left":
            self.left = boolean
        elif direction == "right":
            self.right = boolean
        self.is_active()
        
    def get_direction_status(self, direction):
        if direction == "left":
            return self.left
        elif direction == "right":
            return self.right
        
    def is_active(self):
        self.active = (self.left or self.right)
        return self.active
        
    def is_bind(self):
        return self.bind
    
    def bound(self):
        self.bind = True
        
    def get_position(self):
        return self.current_left, self.current_right
    