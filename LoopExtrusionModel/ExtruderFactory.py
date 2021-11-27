import ExtruderType

class ExtruderFactory:
    
    def get(e_type, stalling_prob=1):
        
        return {
            ExtruderType.COHESIN: Cohesin(stalling_prob),
            ExtruderType.CONDENSIN: Condensin(stalling_prob)
        }.get(e_type,0)