class Move:
    def __init__(self, position):
        self.position = position
    
    def is_within_range(self):
        return (1 <= self.position <= 9)