import Extruder

class Condensin(Extruder):
    
    def stop_i(self):
        return 2
    
    def color(self):
        return "r"
    
    def __str__(self):
        return f"Condensin at {self.get_position()}"