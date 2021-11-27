import numpy as np

class Genome:
        
    def __init__(self, seed, length=10000, cohesin_stopper_gap=100, condensin_stopper_gap=20):
        np.random.default_rng(seed)
        cohesin_stopper_p = 1/cohesin_stopper_gap
        condensin_stopper_p = 1/condensin_stopper_gap
        no_stopper_p = 1 - cohesin_stopper_p - condensin_stopper_p
        self.array = np.random.choice([0, 1, 2], 
                                      size=length, 
                                      p=[no_stopper_p, 
                                         cohesin_stopper_p, 
                                         condensin_stopper_p])
        self.occupited = np.zeros(length, dtype=bool)
        
    def get_length(self):
        return len(self.array)
        
    def get_array(self):
        return self.array
    
    def is_occupited(self, index):
        return self.occupited[index]
    
    def update_occupited(self, index, status=True):
        self.occupited[index] = status
        
    def __str__(self):
        return str(self.array)
            
        