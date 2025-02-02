class Move:
    def __init__(self, position):
        self.position = position
    
    def is_valid(self):
        return (1 <= self.position <= 9)
    
    def get_row(self):
        match self._position:
            case 7 | 8 | 9: return 2
            case 4 | 5 | 6: return 1
            case 1 | 2 | 3: return 0
            
    def get_col(self):
        match self._position:
            case 7 | 4 | 1: return 0
            case 8 | 5 | 2: return 1
            case 9 | 6 | 3: return 2