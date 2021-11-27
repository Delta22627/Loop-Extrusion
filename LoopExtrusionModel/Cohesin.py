import Extruder

class Cohesin(Extruder):
    
    def stop_i(self):
        return 1
    
    def color(self):
        return "b"
    
    def __str__(self):
        return f"Cohesin at {self.get_position()}"